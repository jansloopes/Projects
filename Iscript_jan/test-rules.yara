rule stringjan
{
    strings:
        $my_text_string = "from"
        $my_text_string1 = "import"
        $my_hex_string = { E2 34 A1 C8 23 FB }

    condition:
        $my_text_string or $my_hex_string or $my_text_string1
}
