# API Automation Practice

基于 **Python + Requests** 的接口自动化实战练习。

## 💡 项目说明
本项目实现了对「客达天下」系统的完整业务流接口联调：
1. GET 请求获取验证码 (`uuid`)
2. POST 请求登录，提取鉴权 `Token`
3. POST 请求新增课程
4. GET 请求查询课程列表，动态提取 `course_id`
5. POST 请求上传文件 (`files` 参数)，提取 `fileName`

## 🚀 技术点
- 使用 `User-Agent` 伪装解决 WAF 防火墙 405 拦截问题。
- 熟练进行 JSON 响应解析与动态参数提取。
- 掌握文件上传（`rb` 模式）与鉴权 Header 组装。