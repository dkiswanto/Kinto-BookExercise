print "how old are you? "
age = gets.chomp.reverse

puts "so you are %{age} years old" % {age: age}
