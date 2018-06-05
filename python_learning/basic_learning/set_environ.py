import os
import sys

argvs = sys.argv
cmd = argvs[1]
paths_to_handle = argvs[2:]

if not (cmd == 'add' or cmd == 'del' or cmd == 'export' or cmd == 'batch'):
    print('错误：第一参数是add或者del')
    sys.exit()

if len(paths_to_handle) == 0:
    sys.exit()

env_paths = os.environ['PATH'].split(';')

need_handle = False

if 'add' == cmd:
    for path_to_handle in paths_to_handle:
        need_add = True
        for env in env_paths:
            if env == path_to_handle or env == (path_to_handle + '\\'):
                need_add = False
                break
        if need_add:
            env_paths.append(path_to_handle)
            need_handle = True
        else:
            print('路径[%s]已存在，不能添加' % path_to_handle)

if 'del' == cmd:
    for path_to_handle in paths_to_handle:
        need_del = False
        path_to_del = ''
        for env in env_paths:
            if env == path_to_handle or env == (path_to_handle + '\\'):
                need_del = True
                path_to_del = env
                break

        if need_del:
            env_paths.remove(path_to_del)
            need_handle = True
        else:
            print('路径[%s]不存在，无需删除' % path_to_handle)

if 'export' == cmd:
    file = open(paths_to_handle[0], 'w')
    file.write(os.environ['PATH'])
    file.close()

if 'batch' == cmd:
    fileName, fileSup = os.path.splitext(paths_to_handle[0])
    file = open(fileName + '.bat', 'w')
    file.write('setx PATH "%s"' % os.environ['PATH'])
    file.close()

if need_handle:
    for env_path in env_paths:
        if env_path == '':
            env_paths.remove(env_path)

    new_env_paths = ';'.join(env_paths)
    print('最终路径:', new_env_paths)
    os.environ['PATH'] = new_env_paths

