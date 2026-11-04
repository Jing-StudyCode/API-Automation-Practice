import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"}
response = requests.get("https://kdtx-test.itheima.net/api/captchaImage",headers = headers)
uuid666 = response.json().get("uuid")
test_data = {
    "username":"admin",
    "password":"HM_2023_test",
    "code":"2",
    "uuid":uuid666
}
res_login = requests.post("https://kdtx-test.itheima.net/api/login",headers = headers,json=test_data)
token666 = res_login.json().get("token")
header_data = {"Authorization":token666,"User-Agent":headers["User-Agent"]}
add_course_data = {"name":"Jing的自动化测试课0001",
                   "subject":"6",
                   "applicablePerson":"2",
                   "info":"测试学习"}
res_add_course = requests.post("https://kdtx-test.itheima.net/api/clues/course",headers = header_data,json = add_course_data)
print(f"新增课程状态码:{res_add_course.status_code}")
print(f"新增课程返回数据:{res_add_course.json()}")
###############查询课程列表，获取动态课程ID###########
print("\n------开始查询课程列表获取ID---------")
res_course_list = requests.get("https://kdtx-test.itheima.net/api/clues/course/list",headers = header_data)
course_id = res_course_list.json().get("rows")[0].get("id")
print(f"成功获取动态课程ID:{course_id}")
print("\n-------开始上传合同--------")
res_upload = requests.post("https://kdtx-test.itheima.net/api/common/upload", headers = header_data, files = {"file":open(
    "test.txt", "rb")})
file_name = res_upload.json().get("fileName")
print(f"上传成功，服务器文件名：{file_name}")