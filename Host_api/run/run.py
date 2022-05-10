import time
import unittest
from HwTestReport import HTMLTestReport
from Host_api.commom.send_email import *

cases_path = r'C:\Users\86182\Desktop\unitest_ui_web\Host_api\test_case'
report_path =r'C:\Users\86182\Desktop\unitest_ui_web\Host_api\report'
def runall():
    suite = unittest.defaultTestLoader.discover(start_dir=cases_path,
                                                pattern="test_*.py")

    NowTime = time.strftime("%Y-%m-%d_%H-%M-%S")
    report = report_path + '/' + "testreport{}.html".format(NowTime)
    with open(report,'wb') as f:
        runner = HTMLTestReport(stream=f,
                                verbosity=2,
                                title=r'接口自动化测试报告,测试结果如下：',
                                description=r'用例执行情况：',
                                tester='Chenxianqi'
                                )
        runner.run(suite)

if __name__ == '__main__':
    runall()
    new_report = new_report(report_path)
    send_mail(new_report)