/*
A KBase module: onerepotest
*/

module onerepotest {

    funcdef send_data(UnspecifiedObject params) returns (UnspecifiedObject) authentication required;

    funcdef print_lines(string text) returns (int number_of_lines) authentication required;

    funcdef generate_error(string error) returns () authentication required;

    funcdef get_deploy_config() returns (mapping<string, string> config) authentication required;

    funcdef list_ref_data(string ref_data_path) returns (list<string> files) authentication required;

    funcdef local_sdk_callback(string input) returns (string output, string state) authentication required;

    funcdef copy_scratch_file(string input_file_name, string output_file_name) returns (string state) authentication required;
};