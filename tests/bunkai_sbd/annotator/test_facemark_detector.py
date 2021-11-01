#!/usr/bin/env python3
import unittest

from bunkai.algorithm.bunkai_sbd.annotator.constant import LAYER_NAME_FIRST
from bunkai.algorithm.bunkai_sbd.annotator.facemark_detector import FaceMarkDetector
from bunkai.base.annotation import Annotations, SpanAnnotation

from .annotation_test_base import TestAnnotatorBase, TestInstance


def init_annotation(text: str) -> Annotations:
    annotations = Annotations()
    annotations.add_annotation_layer(
        LAYER_NAME_FIRST,
        [
            SpanAnnotation(
                rule_name=LAYER_NAME_FIRST,
                start_index=len(text) - 1,
                end_index=len(text),
                split_string_type=None,
                split_string_value=None,
            )
        ],
    )
    return annotations


class TestMorphAnnotator(TestAnnotatorBase):
    def test_performance_facemark(self):
        self.test_patterns = {
            "facemark_end": [
                ("いい湯でした(^_^)", 11),
                ("品揃えは良い(^o^)", 11),
                ("品揃えは良い(^^)", 10),
                ("品揃えは良い(^-^)", 11),
                ("サービスは良好（●＾o＾●）", 14),
                ("食事はよかった（＾◇＾）", 12),
                ("食事はよかった(*^_^*)", 14),
                ("品揃えは良い(*´ｰ`)", 12),
                ("サービスは良好(*´∀｀*)", 14),
                ("食事はよかった(*´ω｀*)", 14),
                ("品揃えは良い(*´艸｀*)", 13),
                ("食事はよかった(/ω＼)", 12),
                ("サービスは良好(^_^)V", 13),
                ("食事はよかった(^o^)V", 13),
                ("品揃えは良いヽ(=´▽`=)ﾉ", 15),
                ("いい湯でしたo(^o^)o", 13),
                ("子供連れによい＼(^_^ )( ^_^)／", 21),
                ("サービスは良好σ(^_^)", 13),
                ("食事はよかったσ(´∀｀)", 13),
                ("品揃えは良い!(^^)!", 12),
                ("子供連れによい(^^ゞ", 11),
                ("いい湯でした(^Q^)/", 12),
                ("食事はよかった(^^ゝ", 11),
                ("食事はよかった(^人^)", 12),
                ("サービスは良好(^_-)-☆", 14),
                ("食事はよかった(^з^)-☆", 14),
                ("食事はよかった＼(◎o◎)／", 14),
                ("食事はよかった(@_@)", 12),
                ("品揃えは良い(＠_＠;)", 12),
                ("サービスは良好(# ﾟДﾟ)", 14),
                ("サービスは良好( ・_・)", 13),
                ("いい湯でした(・_・)", 11),
                ("食事はよかった(・o・)", 12),
                ("サービスは良好(｡･･｡)", 13),
                ("品揃えは良い(゜_゜)", 11),
                ("いい湯でした(`_`)ノ゛", 13),
                ("サービスは良好(￣ー￣)ｂ", 13),
                ("子供連れによい(^-^;", 12),
                ("サービスは良好(-_-;)", 13),
                ("いい湯でした(=_=;)", 12),
                ("いい湯でした(ﾉ´Д`)", 12),
                ("サービスは良好(-o-;)", 13),
                ("食事はよかった(^^;)", 12),
                ("子供連れによい(^_^;)", 13),
                ("子供連れによい(^o^;)", 13),
                ("食事はよかった...(((;^^)", 17),
                ("いい湯でした(ﾟεﾟ*)", 12),
                ("食事はよかった♪〜(￣ε￣；)", 15),
                ("品揃えは良い(~o~)m", 12),
                ("品揃えは良い(-.-)zzZZ", 15),
                ("子供連れによい(-_-)zzZZ", 16),
                ("食事はよかった(+_+)", 12),
                ("食事はよかった( ..)ヾ", 13),
                ("食事はよかった(o-_-o)", 14),
                ("サービスは良好ヽ(#ﾟДﾟ)ﾉ", 15),
                ("サービスは良好(-_-メ)", 13),
                ("サービスは良好(ーー゛)", 12),
                ("サービスは良好(-’’-)", 13),
                ("食事はよかった(｀´）", 11),
                ("いい湯でしたヽ(#｀Д´#)ﾉ", 15),
                ("品揃えは良い(￣へ￣井)", 12),
                ("サービスは良好(-ε´-。)", 14),
                ("サービスは良好(￣д￣)", 12),
                ("食事はよかった( ´Д｀)", 13),
                ("サービスは良好(ﾉ´□｀)ﾉ", 14),
                ("いい湯でしたヽ(*´Д｀*)ﾉ", 15),
                ("サービスは良好┐(´〜`；)┌", 15),
                ("子供連れによい(#´Д｀#)", 14),
                ("いい湯でしたヽ(￣▽￣)ﾉ", 13),
                ("いい湯でした(*_*)", 11),
                ("いい湯でした( -_-)", 12),
                ("いい湯でした｜(-_-)｜", 13),
                ("子供連れによい(;_;)", 12),
                ("品揃えは良い(T_T)", 11),
                ("子供連れによい(/_;)", 12),
                ("食事はよかった(ﾉдヽ)", 12),
                ("いい湯でした(TдT)", 11),
                ("いい湯でした(ﾉ´□｀)", 12),
                ("食事はよかったヽ(;´Д`)ノ", 15),
                ("子供連れによい(ｏ´_｀ｏ)", 14),
                ("子供連れによい(^∧^)", 12),
                ("食事はよかったm(_ _)m", 14),
                ("いい湯でした＼(__ )", 12),
                ("品揃えは良い(&gt;_&lt;)", 17),
                ("子供連れによい(&gt;_&lt;)", 18),
                ("いい湯でした(+д+)", 11),
                ("食事はよかった（￣□￣；）", 13),
                ("子供連れによい(lll￣□￣)", 15),
                ("子供連れによいp(^^)q", 13),
                ("品揃えは良い(-o-)y-~~~", 16),
                ("いい湯でした(^_^)y-~~~", 16),
                ("いい湯でした(’A`)y-~", 14),
                ("いい湯でしたφ(..)", 11),
                ("食事はよかったφ(｀д´)", 13),
                ("食事はよかったφ(^o^)", 13),
                ("子供連れによいVo￥oV", 12),
                ("食事はよかった(ΦωΦ)", 12),
                ("食事はよかったU^ｪ^U", 12),
                ("食事はよかった(*￣(ｴ)￣*)", 16),
                ("サービスは良好( ^_^)／□☆□＼(^_^ )", 24),
                ("いい湯でした( ^_^)／ o(^o^)o ＼(^_^ )", 29),
                ("食事はよかった(／＼) ＼(^o^)／", 19),
                ("いい湯でした(^_^)/~~~", 15),
            ],
            "jp_char_after_facemark": [
                ("いい湯でした(^_^)食事はよかった", 11),
                ("サービスは良好(^o^)子供連れによい", 11),
                ("食事はよかった(^^)子供連れによい", 10),
                ("食事はよかった(^-^)品揃えは良い", 11),
                ("サービスは良好（●＾o＾●）食事はよかった", 13),
                ("子供連れによい（＾◇＾）子供連れによい", 11),
                ("子供連れによい(*^_^*)いい湯でした", 13),
                ("品揃えは良い(*´ｰ`)サービスは良好", 12),
                ("子供連れによい(*´∀｀*)サービスは良好", 13),
                ("品揃えは良い(*´ω｀*)サービスは良好", 13),
                ("品揃えは良い(*´艸｀*)サービスは良好", 13),
                ("品揃えは良い(/ω＼)サービスは良好", 11),
                ("食事はよかった(^_^)V食事はよかった", 12),
                ("食事はよかった(^o^)Vサービスは良好", 12),
                ("食事はよかったヽ(=´▽`=)ﾉ子供連れによい", 15),
                ("子供連れによいo(^o^)o品揃えは良い", 13),
                ("子供連れによい＼(^_^ )( ^_^)／品揃えは良い", 20),
                ("子供連れによいσ(^_^)子供連れによい", 12),
                ("子供連れによいσ(´∀｀)子供連れによい", 12),
                ("食事はよかった!(^^)!食事はよかった", 12),
                ("食事はよかった(^^ゞいい湯でした", 10),
                ("サービスは良好(^Q^)/いい湯でした", 12),
                ("子供連れによい(^^ゝいい湯でした", 10),
                ("サービスは良好(^人^)食事はよかった", 11),
                ("いい湯でした(^_-)-☆いい湯でした", 13),
                ("品揃えは良い(^з^)-☆子供連れによい", 13),
                ("食事はよかった＼(◎o◎)／子供連れによい", 13),
                ("サービスは良好(@_@)食事はよかった", 11),
                ("子供連れによい(＠_＠;)サービスは良好", 12),
                ("サービスは良好(# ﾟДﾟ)子供連れによい", 13),
                ("食事はよかった( ・_・)品揃えは良い", 12),
                ("サービスは良好(・_・)子供連れによい", 11),
                ("食事はよかった(・o・)子供連れによい", 11),
                ("サービスは良好(｡･･｡)サービスは良好", 12),
                ("いい湯でした(゜_゜)食事はよかった", 11),
                ("食事はよかった(`_`)ノ゛いい湯でした", 13),
                ("サービスは良好(￣ー￣)ｂ子供連れによい", 12),
                ("品揃えは良い(^-^;子供連れによい", 11),
                ("食事はよかった(-_-;)いい湯でした", 12),
                ("品揃えは良い(=_=;)サービスは良好", 12),
                ("品揃えは良い(ﾉ´Д`)子供連れによい", 12),
                ("サービスは良好(-o-;)子供連れによい", 12),
                ("子供連れによい(^^;)いい湯でした", 11),
                ("子供連れによい(^_^;)サービスは良好", 12),
                ("子供連れによい(^o^;)いい湯でした", 12),
                ("いい湯でした...(((;^^)いい湯でした", 16),
                ("サービスは良好(ﾟεﾟ*)子供連れによい", 12),
                ("サービスは良好♪〜(￣ε￣；)品揃えは良い", 14),
                ("サービスは良好(~o~)m子供連れによい", 12),
                ("いい湯でした(-.-)zzZZ子供連れによい", 15),
                ("品揃えは良い(-_-)zzZZサービスは良好", 15),
                ("食事はよかった(+_+)サービスは良好", 11),
                ("いい湯でした( ..)ヾ食事はよかった", 12),
                ("品揃えは良い(o-_-o)子供連れによい", 13),
                ("いい湯でしたヽ(#ﾟДﾟ)ﾉサービスは良好", 14),
                ("品揃えは良い(-_-メ)サービスは良好", 12),
                ("食事はよかった(ーー゛)食事はよかった", 11),
                ("子供連れによい(-’’-)品揃えは良い", 12),
                ("食事はよかった(｀´）いい湯でした", 10),
                ("いい湯でしたヽ(#｀Д´#)ﾉサービスは良好", 15),
                ("いい湯でした(￣へ￣井)食事はよかった", 12),
                ("サービスは良好(-ε´-。)品揃えは良い", 13),
                ("食事はよかった(￣д￣)食事はよかった", 11),
                ("いい湯でした( ´Д｀)品揃えは良い", 12),
                ("サービスは良好(ﾉ´□｀)ﾉ品揃えは良い", 13),
                ("品揃えは良いヽ(*´Д｀*)ﾉ食事はよかった", 15),
                ("いい湯でした┐(´〜`；)┌子供連れによい", 14),
                ("サービスは良好(#´Д｀#)食事はよかった", 13),
                ("いい湯でしたヽ(￣▽￣)ﾉ食事はよかった", 13),
                ("品揃えは良い(*_*)いい湯でした", 11),
                ("サービスは良好( -_-)食事はよかった", 12),
                ("子供連れによい｜(-_-)｜子供連れによい", 13),
                ("サービスは良好(;_;)食事はよかった", 11),
                ("いい湯でした(T_T)食事はよかった", 11),
                ("いい湯でした(/_;)品揃えは良い", 11),
                ("食事はよかった(ﾉдヽ)サービスは良好", 11),
                ("いい湯でした(TдT)いい湯でした", 11),
                ("子供連れによい(ﾉ´□｀)いい湯でした", 12),
                ("子供連れによいヽ(;´Д`)ノ品揃えは良い", 14),
                ("食事はよかった(ｏ´_｀ｏ)子供連れによい", 13),
                ("品揃えは良い(^∧^)子供連れによい", 11),
                ("子供連れによいm(_ _)m子供連れによい", 13),
                ("いい湯でした＼(__ )子供連れによい", 12),
                ("サービスは良好(&gt;_&lt;)子供連れによい", 17),
                ("子供連れによい(&gt;_&lt;)品揃えは良い", 17),
                ("食事はよかった(+д+)サービスは良好", 11),
                ("食事はよかった（￣□￣；）子供連れによい", 12),
                ("子供連れによい(lll￣□￣)食事はよかった", 14),
                ("子供連れによいp(^^)q子供連れによい", 12),
                ("いい湯でした(-o-)y-~~~品揃えは良い", 16),
                ("いい湯でした(^_^)y-~~~いい湯でした", 16),
                ("子供連れによい(’A`)y-~子供連れによい", 14),
                ("品揃えは良いφ(..)品揃えは良い", 11),
                ("食事はよかったφ(｀д´)食事はよかった", 12),
                ("子供連れによいφ(^o^)食事はよかった", 12),
                ("食事はよかったVo￥oVサービスは良好", 11),
                ("サービスは良好(ΦωΦ)サービスは良好", 11),
                ("子供連れによいU^ｪ^Uいい湯でした", 11),
                ("食事はよかった(*￣(ｴ)￣*)いい湯でした", 15),
                ("いい湯でした( ^_^)／□☆□＼(^_^ )食事はよかった", 23),
                ("いい湯でした( ^_^)／ o(^o^)o ＼(^_^ )食事はよかった", 29),
                ("子供連れによい(／＼) ＼(^o^)／品揃えは良い", 18),
                ("品揃えは良い(^_^)/~~~食事はよかった", 15),
            ],
            "en_char_after_facemark": [
                ("いい湯でした(^_^)MFG", 11),
                ("サービスは良好(^o^)USJ", 11),
                ("いい湯でした(^^)USJ", 10),
                ("いい湯でした(^-^)UBS", 11),
                ("食事はよかった（●＾o＾●）MFG", 13),
                ("子供連れによい（＾◇＾）UFJ", 11),
                ("子供連れによい(*^_^*)SGM", 13),
                ("いい湯でした(*´ｰ`)SGM", 12),
                ("品揃えは良い(*´∀｀*)DB", 13),
                ("品揃えは良い(*´ω｀*)UFJ", 13),
                ("食事はよかった(*´艸｀*)USJ", 13),
                ("品揃えは良い(/ω＼)USJ", 11),
                ("品揃えは良い(^_^)VSGM", 12),
                ("子供連れによい(^o^)VSGM", 12),
                ("サービスは良好ヽ(=´▽`=)ﾉUFJ", 15),
                ("いい湯でしたo(^o^)oMFG", 13),
                ("品揃えは良い＼(^_^ )( ^_^)／DEUTSCH", 20),
                ("サービスは良好σ(^_^)DB", 12),
                ("品揃えは良いσ(´∀｀)SSS", 12),
                ("品揃えは良い!(^^)!DEUTSCH", 12),
                ("いい湯でした(^^ゞSSS", 10),
                ("食事はよかった(^Q^)/DEUTSCH", 12),
                ("食事はよかった(^^ゝDB", 10),
                ("品揃えは良い(^人^)MFG", 11),
                ("いい湯でした(^_-)-☆USJ", 13),
                ("サービスは良好(^з^)-☆BOSH", 13),
                ("いい湯でした＼(◎o◎)／SSS", 13),
                ("子供連れによい(@_@)MFG", 11),
                ("品揃えは良い(＠_＠;)SSS", 12),
                ("サービスは良好(# ﾟДﾟ)SSS", 13),
                ("子供連れによい( ・_・)MFG", 12),
                ("サービスは良好(・_・)SGM", 11),
                ("サービスは良好(・o・)SSS", 11),
                ("いい湯でした(｡･･｡)SGM", 12),
                ("食事はよかった(゜_゜)DB", 11),
                ("品揃えは良い(`_`)ノ゛USJ", 13),
                ("食事はよかった(￣ー￣)ｂSGM", 12),
                ("子供連れによい(^-^;USJ", 11),
                ("いい湯でした(-_-;)UFJ", 12),
                ("いい湯でした(=_=;)DEUTSCH", 12),
                ("品揃えは良い(ﾉ´Д`)BOSH", 12),
                ("サービスは良好(-o-;)USJ", 12),
                ("いい湯でした(^^;)SGM", 11),
                ("いい湯でした(^_^;)DEUTSCH", 12),
                ("子供連れによい(^o^;)USJ", 12),
                ("いい湯でした...(((;^^)SSS", 16),
                ("品揃えは良い(ﾟεﾟ*)UFJ", 12),
                ("食事はよかった♪〜(￣ε￣；)DB", 14),
                ("食事はよかった(~o~)mUFJ", 12),
                ("子供連れによい(-.-)zzZZSGM", 15),
                ("いい湯でした(-_-)zzZZMFG", 15),
                ("サービスは良好(+_+)USJ", 11),
                ("サービスは良好( ..)ヾUSJ", 12),
                ("食事はよかった(o-_-o)SGM", 13),
                ("子供連れによいヽ(#ﾟДﾟ)ﾉDEUTSCH", 14),
                ("いい湯でした(-_-メ)SSS", 12),
                ("いい湯でした(ーー゛)DB", 11),
                ("サービスは良好(-’’-)SSS", 12),
                ("サービスは良好(｀´）MFG", 10),
                ("いい湯でしたヽ(#｀Д´#)ﾉUSJ", 15),
                ("いい湯でした(￣へ￣井)USJ", 12),
                ("サービスは良好(-ε´-。)UBS", 13),
                ("子供連れによい(￣д￣)SSS", 11),
                ("いい湯でした( ´Д｀)BOSH", 12),
                ("食事はよかった(ﾉ´□｀)ﾉBOSH", 13),
                ("子供連れによいヽ(*´Д｀*)ﾉDEUTSCH", 15),
                ("食事はよかった┐(´〜`；)┌SSS", 14),
                ("子供連れによい(#´Д｀#)DEUTSCH", 13),
                ("いい湯でしたヽ(￣▽￣)ﾉSGM", 13),
                ("サービスは良好(*_*)DB", 11),
                ("サービスは良好( -_-)DB", 12),
                ("品揃えは良い｜(-_-)｜DB", 13),
                ("サービスは良好(;_;)DEUTSCH", 11),
                ("いい湯でした(T_T)USJ", 11),
                ("いい湯でした(/_;)UFJ", 11),
                ("品揃えは良い(ﾉдヽ)BOSH", 11),
                ("品揃えは良い(TдT)UFJ", 11),
                ("食事はよかった(ﾉ´□｀)BOSH", 12),
                ("いい湯でしたヽ(;´Д`)ノSSS", 14),
                ("食事はよかった(ｏ´_｀ｏ)UFJ", 13),
                ("サービスは良好(^∧^)SSS", 11),
                ("子供連れによいm(_ _)mSSS", 13),
                ("品揃えは良い＼(__ )SSS", 12),
                ("子供連れによい(&gt;_&lt;)USJ", 17),
                ("食事はよかった(&gt;_&lt;)MFG", 17),
                ("子供連れによい(+д+)UFJ", 11),
                ("子供連れによい（￣□￣；）SGM", 12),
                ("子供連れによい(lll￣□￣)BOSH", 14),
                ("品揃えは良いp(^^)qUBS", 12),
                ("品揃えは良い(-o-)y-~~~BOSH", 16),
                ("品揃えは良い(^_^)y-~~~DEUTSCH", 16),
                ("品揃えは良い(’A`)y-~UFJ", 14),
                ("子供連れによいφ(..)MFG", 11),
                ("サービスは良好φ(｀д´)SSS", 12),
                ("食事はよかったφ(^o^)SSS", 12),
                ("食事はよかったVo￥oVUSJ", 11),
                ("子供連れによい(ΦωΦ)SGM", 11),
                ("品揃えは良いU^ｪ^USGM", 11),
                ("品揃えは良い(*￣(ｴ)￣*)UBS", 15),
                ("サービスは良好( ^_^)／□☆□＼(^_^ )BOSH", 23),
                ("子供連れによい( ^_^)／ o(^o^)o ＼(^_^ )UFJ", 29),
                ("サービスは良好(／＼) ＼(^o^)／USJ", 18),
                ("サービスは良好(^_^)/~~~DEUTSCH", 15),
            ],
        }

        facemark_detector = FaceMarkDetector()
        for pattern_name, tests in self.test_patterns.items():
            fp = tp = fn = 0
            for test_obj in tests:
                ann = init_annotation(test_obj[0])
                ann = facemark_detector.annotate(original_text=test_obj[0], spans=ann)
                sb_positions = list(ann.get_annotation_layer(FaceMarkDetector.__name__))
                if len(sb_positions) > 1:
                    fp += 1
                elif len(sb_positions) == 1 and sb_positions[0].end_index == test_obj[1]:
                    tp += 1
                elif len(sb_positions) == 1 and sb_positions[0].end_index != test_obj[1]:
                    fp += 1
                elif len(sb_positions) == 0:
                    fn += 1
                else:
                    raise Exception()
            p = tp / (tp + fp)
            r = tp / (tp + fn)
            print(f"{pattern_name} precision:{p} = {tp} / {tp + fp} recall:{r} ={tp} / {tp + fn}")

    def test_annotate(self):
        test_instances = [
            TestInstance(text="宿を予約しました＼(^o^)／まだ2ヶ月も先だけど。", n_sentence=2, expected_rules=[FaceMarkDetector.__name__])
        ]
        self.is_check_test_instance(annotator=FaceMarkDetector(), test_cases=test_instances)


if __name__ == "__main__":
    unittest.main()
