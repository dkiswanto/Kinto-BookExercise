def print_two(*args, print_this)
    arg1, arg2 = args
    puts "arg1 : #{arg1}, arg2 : #{arg2}" + " print this : #{print_this}"
end

def print_two_again(arg1, arg2 = "DEFAULT") 
    puts "arg1 : #{arg1}, arg2 : #{arg2}" 
end

def print_none()
    puts "i got nothin."
end

print_two( "Shaw")
print_two_again("Zed")
print_none()

