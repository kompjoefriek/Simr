import pytest
from simr.Configuration.Configuration import Configuration


__author__ = 'Roel van Nuland <roel@kompjoefriek.nl>'

# error situations

def test_no_config():
    with pytest.raises(TypeError):
        Configuration()


def test_non_existing_config():
    with pytest.raises(IOError):
        Configuration("tests/config/non_existing_config.xml")


def test_empty_config():
    with pytest.raises(RuntimeError):
        Configuration("tests/config/empty_config.xml")


def test_variables_cyclic_config():
    with pytest.raises(RuntimeWarning):
        Configuration("tests/config/variables_cyclic_config.xml")


def test_invalid_xml():
    with pytest.raises(RuntimeError):
        Configuration("tests/config/invalid.xml")


# check variables

def checkDefaultVariables(variables):
    index = 0
    assert variables[index].name == "DATE"
    index += 1
    assert variables[index].name == "TIME"
    index += 1
    return index


def test_non_simr_config():
    c = Configuration("tests/config/lorum.ipsum.xml")
    # should this continue to parse without a valid root tag?
    variables = c.get_variables()
    index = checkDefaultVariables(variables)


def test_no_variables():
    c = Configuration("tests/config/main_echo.xml")
    variables = c.get_variables()
    index = checkDefaultVariables(variables)


def test_variables_simple_config():
    c = Configuration("tests/config/variables_simple_config.xml")
    variables = c.get_variables()
    index = checkDefaultVariables(variables)
    #<variable name="MY_PATH" value="C:\My\Folder\Client_v%MY_VERSION%.jar;C:\My\Folder\Server_v%MY_VERSION%.jar" />
    #<variable name="MY_VERSION" value="1.2.3" />
    assert variables[index].name == "MY_PATH"
    assert variables[index].value == "C:\\My\\Folder\\Client_v1.2.3.jar;C:\\My\\Folder\\Server_v1.2.3.jar"
    index += 1
    assert variables[index].name == "MY_VERSION"
    assert variables[index].value == "1.2.3"
    index += 1


def test_variables_complex_config():
    c = Configuration("tests/config/variables_complex_config.xml")
    variables = c.get_variables()
    index = checkDefaultVariables(variables)
    #<variable name="JAVA" value="'C:\Program Files\Java\jre1.8.0_101\bin\java'" />
    #<variable name="TEST_VERSION" value="1.2.3" />
    #<variable name="TEST_PATH" value="C:\My_SDK" />
    #<variable name="CODE_PATH" value="C:\CodeBase" />
    #<variable name="SERVER_PATH" value="%CODE_PATH%\Stuff\MyServer" />
    #<variable name="OUTPUT_PATH" value="C:\Output" />
    #<variable name="CLASSPATH" value="%TEST_PATH%\mysdk\server\server_mysdk_%TEST_VERSION%.jar;%SERVER_PATH%\bin;%CODE_PATH%\bin;%CODE_PATH%\other\bin" />
    assert variables[index].name == "JAVA"
    assert variables[index].value == "'C:\\Program Files\\Java\\jre1.8.0_101\\bin\\java'"
    index += 1
    assert variables[index].name == "TEST_VERSION"
    assert variables[index].value == "1.2.3"
    index += 1
    assert variables[index].name == "TEST_PATH"
    assert variables[index].value == "C:\\My_SDK"
    index += 1
    assert variables[index].name == "CODE_PATH"
    assert variables[index].value == "C:\\CodeBase"
    index += 1
    assert variables[index].name == "SERVER_PATH"
    assert variables[index].value == "C:\\CodeBase\\Stuff\\MyServer"
    index += 1
    assert variables[index].name == "OUTPUT_PATH"
    assert variables[index].value == "C:\\Output"
    index += 1
    assert variables[index].name == "CLASSPATH"
    assert variables[index].value == "C:\\My_SDK\\mysdk\\server\\server_mysdk_1.2.3.jar;C:\\CodeBase\\Stuff\\MyServer\\bin;C:\\CodeBase\\bin;C:\\CodeBase\\other\\bin"
    index += 1


def test_variables_date_config():
    c = Configuration("tests/config/variables_date_config.xml")
    variables = c.get_variables()
    index = checkDefaultVariables(variables)
    #<variable name="MY_PATH_A" value="C:\My\Folder\Client_v%MY_VERSION%.jar;C:\My\Folder\%DATE%\Server_v%MY_VERSION%.jar" />
    #<variable name="MY_PATH_B" value="C:\My\Folder\Client_v%MY_VERSION%.jar;C:\My\Folder\%TIME%\Server_v%MY_VERSION%.jar" />
    #<variable name="MY_VERSION" value="1.2.3" />


# check tasks

def test_task_with_input():
    c = Configuration("tests/config/task_with_input.xml")
    tasks = c.get_tasks()
    #<task>
    #    <command><![CDATA[echo "Hello, input"]]></command>
    #    <input>
    #        <!-- optional, for example when certain input parameters are needed for the command that need to be escaped? -->
    #        <parameter name="key" value="value" />
    #    </input>
    #</task>
    assert len(tasks) == 1
    assert tasks[0].command == "echo"
    # i don't understand why input overrides the parameters
    assert tasks[0].parameters == {"key": "value"}
    assert tasks[0].output == None


def test_task_with_output():
    c = Configuration("tests/config/task_with_output.xml")
    tasks = c.get_tasks()
    #<task>
    #    <command><![CDATA[echo "Hello, output"]]></command>
    #    <output>
    #        <!-- optional redirect for output: log, stdout, etc. -->
    #        <redirect target="stdout" />
    #    </output>
    #</task>
    assert len(tasks) == 1
    assert tasks[0].command == "echo"
    assert len(tasks[0].parameters) == 1
    assert tasks[0].parameters[0] == "Hello, output"
    assert tasks[0].output == "stdout"

