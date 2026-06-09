# Pre_data
전처리 데이터
# 법률 데이터 전처리 및 병합 도구 (JSON to ChatML JSONL)

이 프로젝트는 개별적으로 분산되어 있는 법률 질의응답 JSON 데이터를 수집하여, LLM(대형 언어 모델) 파인튜닝에 적합한 **ChatML(Chat Markup Language)** 포맷의 단일 JSONL(JSON Lines) 파일로 통합 및 전처리하는 파이썬 스크립트입니다.

---

## 📌 주요 기능

* **자동 파일 탐색**: 지정된 데이터 폴더(`data/train`) 내의 모든 `.json` 파일을 자동으로 탐색합니다.
* **데이터 예외 처리 및 타입 정제**:
    * `input` 또는 `output` 데이터가 리스트(List) 형태로 들어오는 경우, 문자열로 자동 변환 및 결합(`join`)하여 유실을 방지합니다.
    * 비정상적인 파일 구조나 손상된 JSON 파일은 `try-except` 구문을 통해 건너뛰어(Skip) 전체 프로세스의 중단을 막습니다.
* **ChatML 포맷팅**: 데이터를 모델 학습에 최적화된 `<|im_start|>system/user/assistant` 구조로 변환합니다.
* **JSONL 변환**: 한 줄에 하나의 JSON 객체가 들어가는 `.jsonl` 형태로 저장하여 대용량 학습 데이터 로드 효율을 높입니다.

---

## 📂 데이터 구조 안내

### 1. 입력 데이터 포맷 (개별 JSON 파일 예시)
`data/train/` 경로에 저장되는 개별 JSON 파일은 반드시 아래와 같이 `taskinfo` 객체 내부에 `input`과 `output` 키를 포함해야 합니다.

```json
{
  "taskinfo": {
    "input": "소송 비용은 누가 부담하나요?",
    "output": "민사소송법 제98조에 따라 소송비용은 패소한 당사자가 부담하는 것이 원칙입니다."
  }
}
