from dovado_rtl.explorers.utilities.tasks import ParsedProject
from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse as general_parse
from dovado_rtl.parsers.system_verilog.system_verilog_parser import SystemVerilogParser
from dovado_rtl.explorers.utilities.design_points import DesignPoint
from typing import Union


def parse(
    input_project: Union[Input, DesignPoint],
) -> Union[ParsedProject, DesignPoint]:
    return general_parse(input_project, SystemVerilogParser)
