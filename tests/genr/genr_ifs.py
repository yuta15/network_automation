import jmespath


from tests.genr.mods.interface.genr_eth import genr_eth
from tests.genr.mods.interface.genr_state import genr_state
from tests.genr.mods.interface.genr_subif import genr_subif


def genr_ifs(int_data, isstate:bool=False, iseth:bool=False, issubif:bool=False) -> dict:
  """
    テストデータを生成する関数
    args:
        int_data: dict
          - interface情報
        eth: bool
          - eth情報を取得する場合はTrueとする。
        subint: bool
          - subint情報を取得する場合はTrueとする。
        subint: state
          - state情報を取得する場合はTrueとする
        →すべてFalseの場合はすべての情報を取得する。
        
    returns:
        return_int_data: dict
          - interface情報を成形したデータ
          {
            interface名: {
                'state': {}
                'ethernet':{},
                'subinterfaces': {}
            }
          }
  """
  isdata = [isstate, iseth, issubif]
  int_name_path = '"openconfig-interfaces:interfaces".interface[*].name'
  eth_path = '"openconfig-interfaces:interfaces".interface[*]'
  state_path = '"openconfig-interfaces:interfaces".interface[*].state'
  subifs_path = '"openconfig-interfaces:interfaces".interface[*].subinterfaces.subinterface[*]'
  if_names = jmespath.search(int_name_path, int_data)
  
  eth_datas = jmespath.search(eth_path, int_data)
  state_datas = jmespath.search(state_path, int_data)
  subifs_datas = jmespath.search(subifs_path, int_data)
  
  cor_eth = genr_eth(eth_datas)
  cor_state = genr_state(state_datas)
  cor_subifs = [genr_subif(subifs_data) for subifs_data in subifs_datas]
  cor_data = {}
  
  for if_name, eth, state, subifs in zip(if_names, cor_eth, cor_state, cor_subifs):
    cor_if_dict = {
      'state': state,
      'ethernet': eth,
      'subinterfaces': subifs
    }
    cor_data[if_name] = cor_if_dict

  if isdata == [False, False, False] or isdata == [True, True, True]:
    return cor_data

  elif isdata == [True, False, False]:
    path = '*.state'
    cor_data = jmespath.search(path, cor_data)
    return cor_data
    
  elif isdata == [True, True, False]:
    path = '*.[state, ethernet]'
    cor_data = jmespath.search(path, cor_data)
    return cor_data
    
  elif isdata == [False, True, False]:
    path = '*.ethernet'
    cor_data = jmespath.search(path, cor_data)
    return cor_data
    
  elif isdata == [False, True, True]:
    path = '*.[ethernet, subinterfaces]'
    cor_data = jmespath.search(path, cor_data)
    return cor_data
    
  elif isdata == [False, False, True]:
    path = '*.subinterfaces'
    cor_data = jmespath.search(path, cor_data)
    return cor_data
    
  elif isdata == [True, False, True]:
    path = '*.[state, subinterfaces]'
    cor_data = jmespath.search(path, cor_data)
    return cor_data