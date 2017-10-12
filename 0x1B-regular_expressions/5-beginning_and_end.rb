#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# regex must be exactly matchin a string that starts by h ends by n and can have a single character in between
puts ARGV[0].scan(/h.n/).join
