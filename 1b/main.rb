# Prompt https://adventofcode.com/2018/day/1

frequency = 0
frequnecies = Hash.new(0)
frequnecies[0] = 1
while true
    File.readlines("input.txt").each do |num|
        frequency += num.to_i
        if frequnecies[frequency] == 1
            puts frequency.to_i
            exit
        else 
            frequnecies[frequency] = 1
        end
    end
    puts frequency
end