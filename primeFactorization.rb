#Aaron Guillen
#October 2016

def primeFactors(x)
	ret = Array.new
	
	if x < 0
		ret.push(-1)
		x *= -1
	elsif x == 0
		ret.push(0)
		return ret
	end
	if x == 1
		ret.push(1)
		return ret
	end
		
	y = 2
	
	while y < ((x / 2) + 1)
		if x % y == 0
			x /= y
			ret.push(y)
		else
			y += 1
		end
	end
	
	ret.push(x)
end

def organizePrint(value)
	print value.to_s + " : 0x" + value.to_s(16) + " : ["
	t1 = Time.now
	primeFactors(value).each  { |x| print " " + x.to_s }
	print " ] : " + (Time.now - t1).to_s
	puts
end

if ARGV.length == 0
	puts "No input?"
elsif ARGV.length == 1
	organizePrint(ARGV[0].to_i)
elsif ARGV.length == 2
	if ARGV[0].to_i < ARGV[1].to_i
		for i in ARGV[0].to_i(0)..ARGV[1].to_i(0)
			organizePrint(i)
		end
	elsif ARGV[0].to_i == ARGV[1].to_i
		organizePrint(ARGV[0].to_i)
	else
		for i in ARGV[1].to_i(0)..ARGV[0].to_i(0)
			organizePrint(i)
		end
	end
end