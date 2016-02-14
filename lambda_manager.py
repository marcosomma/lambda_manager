#!/usr/bin/python2.7
# encoding=utf8
import curses, os

visual_elements = {
    'index_rows': [
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\[ BLACKWOODSEVEN LAMBDA MANAGING INTERFACE ]\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/_____________________________________________________________________|\/|',
        '/|\/                                  |                                  |\/|',
        '/|\/------------[LAMBDA]--------------|--------------[ALIAS]-------------|\/|',
        '/|\/                                  |                                  |\/|',
        '/|\/ 1 - Create Lambda                | 4 - Create Alias                 |\/|',
        '/|\/ 2 - Update Lambda                | 5 - Update Alias                 |\/|',
        '/|\/ 3 - Delete Lambda                | 6 - Delete Alias                 |\/|',
        '/|\/                                  |                                  |\/|',
        '/|\/---------------------------------------------------------------------|\/|',
        '/|\/ q - Exit  | h - help                                                |\/|',
        '/|\/_____________________________________________________________________|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        '/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|',
        'Please select an action: '
    ],
    'questions': {
        'region': ['REGION WHERE DEPLOY THE LAMBDA FUNCTION:'
                   '\n    -Ex: eu-west-1'
                   '\n    http://docs.aws.amazon.com/general/latest/gr/rande.html',
                   3],
        'function_name': ['NAME LAMBDA FUNCTION:'
                          '\n    -Ex: helloword',
                          2],
        'zip_path': ['ABSOLUTE PATH TO THE ZIP FILE:'
                     '\n    -Ex: some/path/myfile.zip',
                     2],
        'iam': ['IAM EXECUTION ROLE:'
                '\n    -Ex: arn:aws:iam::438423213058:role/lambda-custom-app-execution-role'
                '\n    http://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html',
                3],
        'function_handler': ['SET FUNCTION HANDLER:'
                             '\n    -Ex: helloword.handler',
                             2],
        'runtime': ['RUNTIME:'
                    '\n    Options: pytho2.7, java, nodejs',
                    2],
        'profile': ['AWS-CLI ADMIN PROFILE:'
                    '\n    -Ex: admin'
                    '\n    http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html',
                    3],
        'version': ['VERSION FUNCTION:'
                    '\n    -Ex: 6',
                    2],
        'alias_name': ['ALIAS NAME:'
                       '\n    -Ex: PROD',
                       2],
        'cmd_deploy_function': ['ADD COMMANDS:'
                                '\n    [--description <value>]'
                                '\n    [--timeout <value>]'
                                '\n    [--memory-size <value>]'
                                '\n    [--publish | --no-publish]'
                                '\n    [--vpc-config <value>]'
                                '\n    [--cli-input-json <value>]'
                                '\n    [--generate-cli-skeleton]'
                                '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html',
                                9],
        'cmd_update_function': ['ADD COMMANDS:'
                                '\n    [--s3-bucket <value>]'
                                '\n    [--s3-key <value>]'
                                '\n    [--s3-object-version <value>]'
                                '\n    [--cli-input-json <value>]'
                                '\n    [--generate-cli-skeleton]'
                                '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/update-function-code.html',
                                7],
        'cmd_delete_function': ['ADD COMMANDS:'
                                '\n    [--qualifier <value>]'
                                '\n    [--cli-input-json <value>]'
                                '\n    [--generate-cli-skeleton]'
                                '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-function.html',
                                4],
        'cmd_create_alias': ['ADD COMMANDS:'
                             '\n    [--description <value>]'
                             '\n    [--cli-input-json <value>]'
                             '\n    [--generate-cli-skeleton]'
                             '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/create-alias.html',
                             4],
        'cmd_update_alias': ['ADD COMMANDS:'
                             '\n    [--description <value>]'
                             '\n    [--cli-input-json <value>]'
                             '\n    [--generate-cli-skeleton]'
                             '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/update-alias.html',
                             4],
        'cmd_delete_alias': ['ADD COMMANDS:'
                             '\n    [--cli-input-json <value>]'
                             '\n    [--generate-cli-skeleton]'
                             '\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-alias.html',
                             3],
    }
}

input = 0
screen = curses.initscr()
curses.curs_set(1)
curses.setsyx(70, 50)


def question(quest, line=0, add_text=''):
    global screen
    prompt_string = add_text + visual_elements['questions'][quest][0]
    line = line + visual_elements['questions'][quest][1]
    screen.clear()
    screen.addstr(0, 0, prompt_string)
    screen.addstr(line, 0, '|>> ')
    screen.refresh()
    input = screen.getstr(line, 4, 200)
    if len(input) is 0:
        return question(quest, 1, 'ERROR! You have to set some value for this parmeter!\n')
    else:
        return input


def yes_or_not(prompt_string):
    global screen
    screen.clear()
    screen.addstr(0, 0, prompt_string + ' Y/N')
    screen.addstr(1, 0, '|>> ')
    screen.refresh()

    q = screen.getch()
    if q == ord('y') or q == ord('Y'):
        return 1
    else:
        return 0


def execute_cmd(cmd_string):
    os.system('clear')
    a = os.system(cmd_string)
    print 'COMMAND: {0}'.format(cmd_string)
    if a == 0:
        print 'OK! Command executed correctly'
    else:
        print 'ERROR! Command terminated with error'
    raw_input('Press enter')


def get_cmd_deploy_lambda():
    region = question('region')
    function_name = question('function_name')
    path_to_zip_file = question('zip_path')
    execution_role = question('iam')
    handler = question('function_handler')
    runtime = question('runtime')
    profile = question('profile')
    cmd = 'aws lambda create-function --region ' + region \
          + ' --function-name ' + function_name \
          + ' --zip-file fileb://' + path_to_zip_file \
          + ' --role ' + execution_role \
          + ' --handler ' + handler \
          + ' --runtime ' + runtime \
          + ' --profile ' + profile
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_deploy_function')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def get_cmd_update_lambda():
    function_name = question('function_name')
    path_to_zip_file = question('zip_path')
    profile = question('profile')
    new_publish = yes_or_not('PUBLISH A NEW VERSION?')
    publish = ' --publish' if new_publish == 1 else ' --no-publish'
    cmd = 'aws lambda update-function-code --function-name ' + function_name \
          + ' --zip-file fileb://' + path_to_zip_file \
          + ' --profile ' + profile \
          + publish
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_update_function')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def get_cmd_delete_lambda():
    function_name = question('function_name')
    set_version = yes_or_not('DELETE SPECIFIC VERSION?')
    cmd = 'aws lambda delete-function --function-name ' + function_name
    if set_version == 1:
        version = question('version')
        cmd = cmd + ' --qualifier ' + version
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_delete_function')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def get_cmd_create_alias():
    function_name = question('function_name')
    version = question('version')
    name = question('alias_name')
    cmd = 'aws lambda create-alias --function-name ' + function_name \
          + ' --name ' + name \
          + ' --function-version ' + version
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_create_alias')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def get_cmd_update_alias():
    function_name = question('function_name')
    version = question('version')
    name = question('alias_name')
    cmd = 'aws lambda update-alias --function-name ' + function_name \
          + ' --name ' + name \
          + ' --function-version ' + version
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_update_alias')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def get_cmd_delete_alias():
    function_name = question('function_name')
    name = question('alias_name')
    cmd = 'aws lambda delete-alias --function-name ' + function_name \
          + ' --name ' + name
    set_options = yes_or_not('ADD OPTIONAL COMMANDS?')
    if set_options == 1:
        optional_commands = question('cmd_delete_alias')
        cmd = cmd \
              + ' ' \
              + optional_commands
    return cmd


def draw(element):
    global screen
    screen.clear()
    screen.keypad(1)
    for i, row in enumerate(visual_elements[element]):
        screen.addstr(i, 0, row)
    screen.refresh()


def init():
    global screen, input
    while input != ord('q'):
        draw('index_rows')
        input = screen.getch()
        cmd = ''
        if input is curses.KEY_RESIZE:
            return init()
        if input == ord('1'):
            cmd = get_cmd_deploy_lambda()
        if input == ord('2'):
            cmd = get_cmd_update_lambda()
        if input == ord('3'):
            cmd = get_cmd_delete_lambda()
        if input == ord('4'):
            cmd = get_cmd_create_alias()
        if input == ord('5'):
            cmd = get_cmd_update_alias()
        if input == ord('6'):
            cmd = get_cmd_delete_alias()
        if input is ord('1') or \
        input is ord('2') or \
        input is ord('3') or \
        input is ord('4') or \
        input is ord('5') or \
        input is ord('6'):
            curses.endwin()
            execute_cmd(cmd)

    curses.endwin()


init()
