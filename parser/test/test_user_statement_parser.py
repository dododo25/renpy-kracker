import decompressor
import os

from parser.block import Element
from parser.user_statement_parser import parse
from renpy.ast import Label, UserStatement

def test_parse_user_statement_window_show():
    """
    label test:
        show target <- this is our target block
    """
    expected = Element(type='statement-show', value='window show')

    decompressed = decompressor.decompress(os.path.join(os.path.dirname(__file__), 'test_user_statement_parser_window_show.rpyc'))

    assert type(decompressed[0]) == Label
    assert type(decompressed[0].block[0]) == UserStatement
    assert expected == parse(decompressed[0].block[0])

def test_parse_user_statement_window_hide():
    """
    label test:
        hide target <- this is our target block
    """
    expected = Element(type='statement-hide', value='window hide')

    decompressed = decompressor.decompress(os.path.join(os.path.dirname(__file__), 'test_user_statement_parser_window_hide.rpyc'))

    assert type(decompressed[0]) == Label
    assert type(decompressed[0].block[0]) == UserStatement
    assert expected == parse(decompressed[0].block[0])

def test_parse_user_statement_window_auto():
    """
    label test:
        hide target <- this is our target block
    """
    expected = Element(type='statement-auto', value='window auto')

    decompressed = decompressor.decompress(os.path.join(os.path.dirname(__file__), 'test_user_statement_parser_window_auto.rpyc'))

    assert type(decompressed[0]) == Label
    assert type(decompressed[0].block[0]) == UserStatement
    assert expected == parse(decompressed[0].block[0])

def test_parse_user_statement_pause():
    """
    label test:
        pause 1.0 <- this is our target block
    """
    expected = Element(type='statement', value='pause 1.0')

    decompressed = decompressor.decompress(os.path.join(os.path.dirname(__file__), 'test_user_statement_parser_pause.rpyc'))

    assert type(decompressed[0]) == Label
    assert type(decompressed[0].block[0]) == UserStatement
    assert expected == parse(decompressed[0].block[0])
