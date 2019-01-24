import pytest
import filter_pandoc_run_py

def test_figattr_convertion():
    s = '"#fig:1 width=5in"'

    fig_s, kw_list_tuple = filter_pandoc_run_py.figattr_str_convertion(s)
    assert fig_s == 'fig:1'
    assert isinstance(kw_list_tuple, list)
    assert isinstance(kw_list_tuple[0], tuple)
    assert kw_list_tuple[0][0] == 'width'
    assert kw_list_tuple[0][1] == '5in'