# Prompt https://adventofcode.com/2018/day/2

boxes = File.open("input.txt").read
boxes = boxes.split("\n").map(&:strip)
answer = "Shit."
File.readlines("input.txt").each do |box_id|
    box_id = box_id.strip
    tracker = Hash.new(0)
    box_id.each_char do |x|
        tracker[x] += 1
    end

    boxes.each do |box|
        diff_chars_count = 0
        box.length.times.each do |x|
            if box[x] != box_id[x]
                diff_chars_count += 1
            end
        end
        if diff_chars_count == 1
            puts "First box: #{box_id}"
            puts "Second box: #{box}"
            answer = (box_id.scan(/./) & box.scan(/./))
        end
    end
end

puts "Answer #{answer.join('')}"