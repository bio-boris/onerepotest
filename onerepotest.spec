/*
A KBase module: onerepotest
*/

module onerepotest {

    funcdef send_data(UnspecifiedObject params) returns (UnspecifiedObject) authentication required;

    funcdef print_lines(string text) returns (int number_of_lines) authentication required;

    funcdef generate_error(string error) returns () authentication required;

    funcdef get_deploy_config() returns (mapping<string, string> config) authentication required;
};