import pandas as pd
df = pd.read_csv('Maligno_y_Benigno.csv')
columna_sentencias = df['Sentence']
arreglo_palabras = columna_sentencias.str.split().tolist()
feature = {
    'F1': 'select',
    'F2': 'union',
    'F3': 'update',
    'F4': 'set',
    'F5': 'alter',
    'F6': 'where',
    'F7': 'like',
    'F8': 'from',
    'F9': 'table',
    'F10': 'database',
    'F11': 'drop',
    'F12': 'delete',
    'F13': 'insert',
    'F14': 'And | Or',
    'F15': 'null',
    'F16': '=',
    'F17': 'information_schema',
    'F18': 'user',
    'F19': 'version',
    'F20': 'load_file',
    'F21': 'save',
    'F22': '! | # | % | $ | NUL | SOH | STX | ETX | EOT | @',
    'F23': '&',
    'F24': '|',
    'F25': ',',
    'F26': ';',
    'F27': '\\',
    'F28': '+ | - | * | /',
    'F29': 'commit | rollback | grant | revoke | declare | remove',
    'F30': 'count(;)',
    'F31': '/* | */',
    'F32': '\\x',
    'F33': '\\u',
    'F34': 'connection',
    'F35': 'xor',
    'F36': 'inner join',
    'F37': 'file | load_file | load_data_infile | into_outfile | into_dumpfile',
    'F38': 'OS | Operative System | exec',
    'F39': 'count(STRING)',
    'F40': 'count(SUBSTR)',
    'F41': 'count(SUBSTRING)',
    'F42': 'count(MID)',
    'F43': 'count(ASC)',
    'F44': 'count(<)',
    'F45': 'count(>)',
    'F46': 'count(")',
    'F47': 'count("")',
    'F48': 'exists',
    'F49': 'floor',
    'F50': 'rand',
    'F51': 'group',
    'F52': 'order',
    'F53': 'lenght',
    'F54': 'ascii',
    'F55': 'if',
    'F56': 'count',
    'F57': 'sleep',
    'F58': 'between',
    'F59': 'values',
    'F60': 'delay',
    'F61': 'wait',
    'F62': 'benchmark',
    'F63': 'indentity_insert',
    'F64': 'truncate table',
    'F65': 'username | password',
    'F66': 'user | pass',
    'F67': '")"',
    'F68': 'limit',
    'F69': 'concat',
    'F70': 'ne',
    'F71': 'find',
    'F72': 'eq | gt | gte | lt | it | lte | ite | in | nin',
    'F73': 'mod | regex | text',
    'F74': 'return',
    'F75': 'return true | return 1',
    'F76': 'exists',
    'F77': 'create',
    'F78': 'show',
    'F79': 'collection',
    'F80': 'while(loop)',
    'F81': 'hidden equality expression',
    'F82': 'large expression'}
feature = [
    'select',
    'union',
    'update',
    'set',
    'alter',
    'where',
    'like',
    'from',
    'table',
    'database',
    'drop',
    'delete',
    'insert',
    'And | Or',
    'null',
    '=',
    'information_schema',
    'user',
    'version',
    'load_file',
    'save',
    '! | # | % | $ | NUL | SOH | STX | ETX | EOT | @',
    '&',
    '|',
    ',',
    ';',
    '+ | - | * | /',
    'commit | rollback | grant |revoke | declare | remove',
    'count(;)',
    '/* | */',
    '\\x',
    '\\u',
    'connection',
    'xor',
    'inner join',
    'file | load_file | load_data_infile | into_outfile | into_dumpfile',
    'OS | Operative System | exec',
    'count(STRING)',
    'count(SUBSTR)',
    '\\',
    'count(SUBSTRING)',
    'count(MID)',
    'count(ASC)', 
    'count(<)',
    'count(>)',
    'count(")',
    'count("")',
    'exists',
    'floor',
    'rand',
    'group',
    'order',
    'lenght',
    'ascii',
    'if',
    'count',
    'sleep',
    'between',
    'values',
    'delay',
    'wait',
    'benchmark'
    'indentity_insert',
    'truncate table',
    'username | password',
    'user | pass',
    '")"',
    'limit',
    'concat',
    'ne',
    'find',
    'eq | gt | gte | lt | it | lte | ite | in | nin',
    'mod | regex | text',
    'return',
    'return true | return 1',
    'exists', 
    'create',
    'show',
    'collection',
    'while(loop)',
    'hidden equality expression',
    'large expression',
]

funcion_conversion = lambda palabra: 1 if palabra in feature else 0

df['SentenciaConvertida'] = columna_sentencias.apply(lambda sentencia: [funcion_conversion(palabra) for palabra in sentencia.split()])

df_nuevo=df[['SentenciaConvertida']]
df_nuevo.to_csv('nuevo_dataset.csv', index=False)
print(df_nuevo)

