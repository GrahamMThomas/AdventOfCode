# Prompt https://adventofcode.com/2018/day/5

require "awesome_print"

polymer_alphabet = Hash.new(0)

('a'..'z').to_a.each do |letter|
    polymer = File.open('input.txt').read
    done = false

    while not done
        skip_index = 0
        tmp_polymer = polymer
        tmp_polymer.gsub!(letter, '')
        tmp_polymer.gsub!(letter.upcase, '')
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
    polymer_alphabet[letter] = tmp_polymer.length
end
ap polymer_alphabet.min_by {|k,v| v}