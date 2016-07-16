filename = ARGV.first

txt = open(filename) #text variable object

puts "Here's your file #{filename} : "
print txt.read

txt.close()
