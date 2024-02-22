## 프로젝트 개요

AskUp은 팀 내에서의 효율적이고 편리한 커뮤니케이션을 위해 ChatGPT를 Slack 채널에 통합하는 프로젝트입니다.

AWS Lambda, SQS 큐 및 API Gateway를 활용하여 AskUp은 Slack 환경 내에서 ChatGPT API에 직접 액세스할 수 있도록 지원합니다.

## 프로젝트 목적

AskUp의 주요 목적은 팀 협업과 생산성을 향상시키기 위해 Slack 채널 내에서 ChatGPT의 기능에 즉시 액세스할 수 있도록 하는 것입니다.

이 통합을 통해 팀 멤버들은 Slack 인터페이스를 떠나지 않고도 자연어 쿼리를 사용하여 빠르게 응답을 생성하고 정보를 수집하거나 아이디어를 떠올릴 수 있습니다.

##프로젝트 목표
- 실시간 상호작용을 위해 Slack 채널 내에서 ChatGPT 통합 기능 제공
- AWS Lambda 및 SQS 큐를 활용하여 Slack 환경 내에서 적시에 응답 보장
- 팀 내 커뮤니케이션 및 의사결정 과정을 간소화
- ChatGPT의 기능을 사용하기 위한 사용자 친화적이고 효율적인 인터페이스 제공

## 기술 스텍
- **AWS Lambda:** ChatGPT 요청의 로직 처리 담당
- **AWS SQS:** Slack 이벤트와 Lambda 함수 간의 통신을 용이하게 함
- **API Gateway (REST):** Slack에서 HTTP 요청을 통해 Lambda 함수를 호출할 수 있는 진입점 역할
- **Python:** 프로젝트의 백엔드 로직 및 ChatGPT 통합에 사용되는 프로그래밍 언어

## 구성 요소
- **Lambda:** ChatGPT 요청 처리 및 응답 생성 담당
- **API Gateway (REST):** Slack에서 Lambda 함수를 트리거하기 위한 진입점 역할 수행
- **SQS:** Slack의 3초 응답 요구 사항을 우회하여 요청을 적시에 처리할 수 있도록 중간 단계 역할 수행

## Github Clone
```bash
git clone https://github.com/dongkoony/AskUp.git
```
