import os
import glob
import json


def merge_and_preprocess():
    DATASET_FOLDER = "data/train"
    OUTPUT_FILE = "law_train_dataset.jsonl"

    file_pattern = os.path.join(DATASET_FOLDER, "*.json")
    all_files = glob.glob(file_pattern)

    print(f"▶ 총 {len(all_files)}개의 JSON 파일을 전처리 및 병합 시작합니다...")

    success_count = 0
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        for file in all_files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = json.load(f)

                    taskinfo = content.get("taskinfo", {})
                    if not isinstance(taskinfo, dict):
                        continue

                    user_input = taskinfo.get("input", "")
                    bot_output = taskinfo.get("output", "")

                    # 리스트 타입 에러 원천 차단 (글자로 강제 병합)
                    if isinstance(user_input, list):
                        user_input = " ".join([str(i) for i in user_input])
                    if isinstance(bot_output, list):
                        bot_output = " ".join([str(o) for o in bot_output])

                    # ChatML 포맷으로 구조화하여 정제
                    if user_input and bot_output:
                        formatted_text = (
                            "<|im_start|>system\n당신은 대한민국의 민사소송 절차와 법률 지식을 안내하는 전문 법률 챗봇입니다.<|im_end|>\n"
                            f"<|im_start|>user\n{user_input}<|im_end|>\n"
                            f"<|im_start|>assistant\n{bot_output}<|im_end|>"
                        )

                        # .jsonl 형식에 맞게 한 줄씩 딕셔너리로 저장
                        json.dump({"text": formatted_text}, outfile, ensure_ascii=False)
                        outfile.write('\n')
                        success_count += 1
            except Exception:
                continue

    print(f"🎉 전처리 완료! 성공적으로 병합된 데이터: {success_count}개 ➡️ 저장 파일: {OUTPUT_FILE}")


if __name__ == "__main__":
    merge_and_preprocess()