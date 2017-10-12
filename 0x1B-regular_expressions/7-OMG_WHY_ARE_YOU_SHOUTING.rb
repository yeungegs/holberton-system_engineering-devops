#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
# The regular expression must only match capital letters
puts ARGV[0].scan(/[A-Z]/).join

