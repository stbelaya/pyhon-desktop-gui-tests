import pytest
import os.path
from comtypes.client import CreateObject

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:/Sync/AddressBook/AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xl(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_xl(file):
    xl = CreateObject("Excel.Application")
    xl.Visible = 0
    try:
        wb = xl.Workbooks.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.xlsx"))
        try:
            data = []
            row_count = wb.Worksheets["Лист1"].UsedRange.Rows.Count
            for i in range(row_count):
                data.append(wb.Worksheets["Лист1"].cells(i+1, 1).Value())
            return data
        finally:
            wb.close()
            xl.quit()
    except FileNotFoundError:
        print(f"File data/{file}.xlsx is not found")
    except:
        print("File related error")



