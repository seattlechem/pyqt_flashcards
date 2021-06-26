import pytest
from datetime import date
from db.db_convert_csv import convert_str_datetime


class TestDateObj:
    def test_convert_str_dateobject(self, date_str: str):
        date_obj = convert_str_datetime(date_str)
        assert(date_obj, date(2021, 6, 17))

if "__name__" == "__main__":
    ts = TestDateObj()
    ts.test_convert_str_dateobject('2021/06/17')
