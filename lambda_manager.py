#!/usr/bin/python2.7
# encoding=utf8
import curses, os

input = 0
screen = curses.initscr()
curses.curs_set(1)
curses.setsyx(50,200)

def question(prompt_string, line):
     global screen
     screen.clear()
     screen.addstr(0, 0, prompt_string)
     screen.addstr( line , 0, "|>> ")
     screen.refresh()
     input = screen.getstr( line , 4, 200)
     if len(input) is 0:
          if "ERROR!" not in prompt_string:
               prompt_string = 'ERROR! You have to set some value for this parmeter!\n'+prompt_string
               line = line + 1
          return question(prompt_string, line)
     else:
          return input

def yes_or_not(prompt_string):
     global screen
     screen.clear()
     screen.addstr(0, 0, prompt_string + " Y/N")
     screen.addstr(1, 0, "|>> ")
     screen.refresh()

     q = screen.getch()
     if q == ord('y') or q == ord('Y'):
          return 1
     else:
          return 0

def execute_cmd(cmd_string):
     os.system("clear")
     a = os.system(cmd_string)
     print "COMMAND: {0}".format(cmd_string)
     if a == 0:
          print "OK! Command executed correctly"
     else:
          print "ERROR! Command terminated with error"
     raw_input("Press enter")

def print_index():
     global screen
     screen.clear()
     screen.keypad(1)
     screen.addstr(0, 0, "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
     screen.addstr(1, 0, "|||||||||||||||[ BLACKWOODSEVEN LAMBDA MANAGING INTERFACE ]||||||||||||||||||")
     screen.addstr(2, 0, "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
     screen.addstr(3, 0, "||||_____________________________________________________________________||||")
     screen.addstr(4, 0, "||||                                  |                                  ||||")
     screen.addstr(5, 0, "||||------------[LAMBDA]--------------|--------------[ALIAS]-------------||||")
     screen.addstr(6, 0, "||||                                  |                                  ||||")
     screen.addstr(7, 0, "|||| 1 - Deploy Lambda Function.      | 4 - Create Alias.                ||||")
     screen.addstr(8, 0, "|||| 2 - Update Lambda Function.      | 5 - Update Alias.                ||||")
     screen.addstr(9, 0, "|||| 3 - Delete Lambda Function.      | 6 - Delete Alias                 ||||")
     screen.addstr(10, 0, "||||                                  |                                  ||||")
     screen.addstr(11, 0, "||||---------------------------------------------------------------------||||")
     screen.addstr(12, 0, "|||| q - Exit                                                            ||||")
     screen.addstr(13, 0, "||||_____________________________________________________________________||||")
     screen.addstr(14, 0, "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
     screen.addstr(15, 0, "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
     screen.addstr(16, 0, "Please select an action: ")
     screen.refresh()

def get_cmd_deploy_lambda():
     region = question("REGION WHERE DEPLOY THE LAMBDA FUNCTION:"
                       "\n    -Ex: eu-west-1"
                       "\n    http://docs.aws.amazon.com/general/latest/gr/rande.html",
                       3)
     function_name = question("NAME LAMBDA FUNCTION:"
                              "\n    -Ex: helloword",
                              2)
     path_to_zip_file = question("ABSOLUTE PATH TO THE ZIP FILE:"
                                 "\n    -Ex: some/path/myfile.zip",
                                 2)
     execution_role = question("IAM EXECUTION ROLE:"
                               "\n    -Ex: arn:aws:iam::438423213058:role/lambda-custom-app-execution-role"
                               "\n    http://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html",
                               3)
     handler = question("SET FUNCTION HANDLER:"
                        "\n    -Ex: helloword.handler",
                        2)
     runtime = question("RUNTIME:"
                        "\n    Options: pytho2.7, java, nodejs",
                        2)
     profile = question("AWS-CLI ADMIN PROFILE:"
                        "\n    -Ex: admin"
                        "\n    http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html",
                        3)
     cmd="aws lambda create-function --region "+ region \
         +" --function-name "+ function_name \
         +" --zip-file fileb://"+ path_to_zip_file \
         +" --role "+ execution_role \
         +" --handler "+ handler \
         +" --runtime "+ runtime \
         +" --profile " + profile
     set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
     if set_options == 1:
          optional_commands = question("ADD COMMANDS:"
                                       "\n    [--description <value>]"
                                       "\n    [--timeout <value>]"
                                       "\n    [--memory-size <value>]"
                                       "\n    [--publish | --no-publish]"
                                       "\n    [--vpc-config <value>]"
                                       "\n    [--cli-input-json <value>]"
                                       "\n    [--generate-cli-skeleton]"
                                       "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html",
                                       9 )
          cmd = cmd \
                + " " \
                + optional_commands
     return cmd

def get_cmd_update_lambda():
    function_name = question("NAME LAMBDA FUNCTION:"
                             "\n    -Ex: helloword",
                             2)
    path_to_zip_file = question("ABSOLUTE PATH TO THE ZIP FILE:"
                                "\n    -Ex: some/path/myfile.zip",
                                2)
    profile = question("AWS-CLI ADMIN PROFILE:"
                        "\n    -Ex: admin"
                        "\n    http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html",
                        3)
    new_publish = yes_or_not("PUBLISH A NEW VERSION?")
    publish = " --publish"if new_publish == 1 else " --no-publish"
    cmd = "aws lambda update-function-code --function-name "+ function_name \
           +" --zip-file fileb://"+ path_to_zip_file \
           +" --profile " + profile \
           + publish
    set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
    if set_options == 1:
        optional_commands = question("ADD COMMANDS:"
                                      "\n    [--s3-bucket <value>]"
                                      "\n    [--s3-key <value>]"
                                      "\n    [--s3-object-version <value>]"
                                      "\n    [--cli-input-json <value>]"
                                      "\n    [--generate-cli-skeleton]"
                                      "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/update-function-code.html",
                                      7 )
        cmd = cmd \
                + " " \
                + optional_commands
    return cmd

def get_cmd_delete_lambda():
     function_name = question("NAME LAMBDA FUNCTION:"
                              "\n    -Ex: helloword",
                              2)
     set_version = yes_or_not("DELETE SPECIFIC VERSION?")
     cmd = "aws lambda delete-function --function-name " + function_name
     if set_version == 1:
          version = question("VERSION:"
                             "\n    -Ex: 6",
                             2)
          cmd = cmd + " --qualifier "+version
     set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
     if set_options == 1:
          optional_commands = question("ADD COMMANDS:"
                                       "\n    [--qualifier <value>]"
                                       "\n    [--cli-input-json <value>]"
                                       "\n    [--generate-cli-skeleton]"
                                       "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-function.html",
                                       4 )
          cmd = cmd \
                + " " \
                + optional_commands
     return cmd

def get_cmd_create_alias():
     function_name = question("NAME LAMBDA FUNCTION:"
                              "\n    -Ex: helloword",
                              2)
     version = question("VERSION LAMBDA FUNCTION:"
                        "\n    -Ex: 6",
                        2)
     name = question("ALIAS NAME:"
                     "\n    -Ex: PROD",
                     2)
     cmd = "aws lambda create-alias --function-name " + function_name \
           + " --name " + name \
           + " --function-version " + version
     set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
     if set_options == 1:
          optional_commands = question("ADD COMMANDS:"
                                       "\n    [--description <value>]"
                                       "\n    [--cli-input-json <value>]"
                                       "\n    [--generate-cli-skeleton]"
                                       "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/create-alias.html",
                                       4 )
          cmd = cmd \
                + " " \
                + optional_commands
     return cmd

def get_cmd_update_alias():
     function_name = question("NAME LAMBDA FUNCTION:"
                              "\n    -Ex: helloword",
                              2)
     version = question("Set NEW function version."
                        "\n    -Ex: 6",
                        2)
     name = question("ALIAS NAME:"
                     "\n    -Ex: PROD",
                     2)
     cmd = "aws lambda update-alias --function-name " + function_name \
           + " --name " + name \
           + " --function-version " + version
     set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
     if set_options == 1:
          optional_commands = question("ADD COMMANDS:"
                                       "\n    [--description <value>]"
                                       "\n    [--cli-input-json <value>]"
                                       "\n    [--generate-cli-skeleton]"
                                       "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/update-alias.html",
                                       4 )
          cmd = cmd \
                + " " \
                + optional_commands
     return cmd

def get_cmd_delete_alias():
     function_name = question("NAME LAMBDA FUNCTION:"
                              "\n    -Ex: helloword",
                              2)
     name = question("ALIAS NAME:"
                     "\n    -Ex: PROD",
                     2)
     cmd = "aws lambda delete-alias --function-name " + function_name \
           + " --name " + name
     set_options = yes_or_not("ADD OPTIONAL COMMANDS?")
     if set_options == 1:
          optional_commands = question("ADD COMMANDS:"
                                       "\n    [--cli-input-json <value>]"
                                       "\n    [--generate-cli-skeleton]"
                                       "\n    http://docs.aws.amazon.com/cli/latest/reference/lambda/delete-alias.html",
                                       3 )
          cmd = cmd \
                + " " \
                + optional_commands
     return cmd

def init():
     global screen, input
     while input != ord('q'):
          print_index()
          input = screen.getch()
          cmd=''
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
          input is ord('6') :
               curses.endwin()
               execute_cmd(cmd)

     curses.endwin()

init()