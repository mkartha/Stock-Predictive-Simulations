let () =
  Out_channel.with_open_text "my_file.txt" (fun oc ->
    Out_channel.output_string oc "Hello, OCaml!\n";
    Out_channel.output_string oc "This is a simple file.\n"
  );
  print_endline "File 'my_file.txt' created and written to using with_open_text."
