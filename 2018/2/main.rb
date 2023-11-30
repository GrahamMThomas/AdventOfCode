# Prompt https://adventofcode.com/2018/day/2

num_of_threes = 0
num_of_twos = 0
File.readlines("input.txt").each do |box_id|
    box_id = box_id.strip
    tracker = Hash.new(0)
    box_id.each_char do |x|
        tracker[x] += 1
    end
    occurance_tracker = tracker.each_with_object({}){|(k,v),o|(o[v]||=[])<<k}
    occurance_tracker.default = []

    num_of_threes += 1 unless occurance_tracker[3].empty?
    num_of_twos += 1 unless occurance_tracker[2].empty?
end
puts "Number of threes #{num_of_threes}"
puts "Number of twos #{num_of_twos}"
puts "Answer #{num_of_threes * num_of_twos}"