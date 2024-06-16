from noa.network_functions.interface.interface import interface
from tests.genr.genr_ifs import genr_ifs


def test_if(conf):
    """
    interfaceをテストする関数
        return: dict
    {
        interface_name:{
            'state': {}
            'ethernet':{},
            'subinterfaces': {}
        }
    }
    """
    paths = ['.', '"openconfig-interfaces:interfaces".interface']
    if_data, if_args = conf(paths)
    cor_if_data = genr_ifs(if_data)
    cor_data = []
    for key, val in zip(list(cor_if_data.keys()), list(cor_if_data.values())):
        cor_dict = {}
        cor_dict[key] = val
        cor_data.append(cor_dict)
    returned_int_data = []
    
    for int_arg in if_args:
        returned_int_data.append(interface(int_arg))

    assert returned_int_data == cor_data