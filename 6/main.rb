# Prompt https://adventofcode.com/2018/day/4

require "awesome_print"

class Step
    attr_accessor :prereqs, :unlocks, :letter

    def initialize
        letter = ''
        @prereqs = []
        @unlocks = []
    end
end

graph = Hash.new { |h,k| h[k] = Step.new }

File.readlines("input.txt").each do |step|
    parsed_step = /Step (\w) must be finished before step (\w) can begin./.match(step.strip())
    prereq = parsed_step.captures[0]
    target = parsed_step.captures[1]
    graph[prereq].letter = prereq
    graph[target].letter = target

    graph[target].prereqs << graph[prereq]
    graph[prereq].unlocks << graph[target]
end

starting_point = graph.select {|k,v| v.prereqs == []}.sort.map(&:first)

answer = []

queue = [starting_point].flatten
while queue.length > 0
    queue.sort!
    letter = queue.delete_at(0)
    answer << letter
    graph[letter].unlocks.map(&:letter).each do |unlock|
        queue << unlock if (graph[unlock].prereqs.map(&:letter) - answer).length.zero?
    end
    # sleep 1
    # puts "Answer: "
    # ap answer
    # sleep 1
    # puts "Queue: "
    # ap queue
end

graph.each do |h,k|
    puts "Letter: #{h} Prereqs: #{k.prereqs.map(&:letter)}"
end

puts answer.join('')