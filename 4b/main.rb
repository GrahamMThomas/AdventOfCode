# Prompt https://adventofcode.com/2018/day/4

require "awesome_print"

guard_sleep_times = Hash.new(0)
guard_sleep_minute_tracker = Hash.new { |h,k| h[k] = Hash.new(0) }
current_guard_id = 0
current_sleep_start_time = 0

File.readlines("input.txt").each do |event|
    parsed_event = /\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] (Guard #(\d+) begins shift|falls asleep|wakes up)/.match(event.strip())
    minute = parsed_event.captures[0].to_i
    event_type = parsed_event.captures[1]

    if event.include? "falls asleep"
        current_sleep_start_time = minute
    elsif event.include? "wakes up"
        guard_sleep_times[current_guard_id] += (minute - current_sleep_start_time)
        ((current_sleep_start_time)..(minute-1)).each do |time|
            guard_sleep_minute_tracker[current_guard_id][time] += 1
        end
    elsif event.include? "begins shift"
        puts "Beginning shift for #{current_guard_id}"
        current_guard_id = parsed_event.captures[2]
    else
        raise "Failed to match event. #{event}"
    end
end

answer = Hash[guard_sleep_times.sort_by{|k,v| v.to_i}]
guard = [answer.max_by{|k,v| v}][0][0]
puts "Laziest Guard is ##{guard}"
ap guard_sleep_minute_tracker[guard]
puts "Most often asleep at #{guard_sleep_minute_tracker[guard].max_by{|k,v| v}.first}"
guard_sleep_minute_tracker.each do |k, v|
    puts "##{k} sleep most times: #{v.max_by{|k,v| v}}"
end