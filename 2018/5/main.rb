# Prompt https://adventofcode.com/2018/day/5

require "awesome_print"

polymer = File.open('input.txt').read

done = false

while not done
    skip_index = 0
    tmp_polymer = polymer
    done = true

    (0...polymer.length-1).each do |x|
        x -= skip_index
        if polymer[x] != polymer[x+1] and polymer[x].downcase == polymer[x+1].downcase
            tmp_polymer.slice!(x+1)
            tmp_polymer.slice!(x)
            skip_index += 2
            done = false
        end
    end
    polymer = tmp_polymer
end

puts polymer.length