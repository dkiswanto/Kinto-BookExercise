user_name = ARGV.first
#user_name = gets.chomp
prompt = "> "

puts "Hi #{user_name}"
puts "Ask something to me!?"
puts prompt
answer = $stdin.gets.chomp

puts "Output the question : #{answer}"
