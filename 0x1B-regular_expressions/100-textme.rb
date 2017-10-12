#!/usr/bin/env ruby
#puts ARGV[0].scan(/\[([^S|A|B|F||u\]]+?)\]/).join(", ").scan(/<([^>]*)>/).last.first
str = ARGV[0].scan(/\[([^\]([TFSu])]*)\]/).join(", ")
str.split(/\w+:(.*), to:(.*), flags:(.*)/)
puts str

