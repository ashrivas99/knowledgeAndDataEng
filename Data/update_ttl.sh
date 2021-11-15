for prop_file in "Mappings/configs"/*
 do
   printf "\n%s \n" "$prop_file"
    java -jar r2rml/r2rml.jar "$prop_file"
   printf "\n \n"
 done