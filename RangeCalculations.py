class Positions

positions - any of 1-6 (6max)
pos1 = positions.UTG
pos2 = positions.BTN
range1 = positions.UTG
range2 = positions.BTN

#this function takes two positions, opening range, and calculates calling range for 2nd position 
#keep turncards empty unless there is a flop/turn/river, otherwise it adapts naturally
#take 
def callingrange(rng1,pos1,pos2,turncards)
	street = preflop
	if turncards==3
		street=flop
	elseif turncards==4
		street=turn
	elseif turncards==5
		street=river

	if street=preflop
		equity = equilab(pos1,pos2)
	end
	if street=flop
		equilab.flopchangecards(turncards(1:3))
		equity = equilab(pos1,pos2)
	end
	if street=turn
		equilab.flopchangecards(turncards(1:3))
		equilab.turn(turncards(4))
		equity = equilab(pos1,pos2)
	end
	if street=river
		equilab.flopchangecards(turncards(1:3))
		equilab.turn(turncards(4))
		equilab.river(turncards(5))
		equity = equilab(pos1,pos2)
	end

#this takes the flops generated and orders them according to the equity of one player
def generatefloporder(pos1,pos2)
	flops = emptydatastoragemechanism
	range1 = pos1.openrange
	range2 = calccallingrangebpositions(range1,pos1,pos2) %no turn cards for now

	%flop generation - some permutation shit
	numflops = 52*51*50
	flops = [3xnumflops] %3 cards each flop, a given number of flops
	count=;	%count tracks the flop # we're on
	for i = 1:52
		flops(count,1) = deck(i)
		count = count+1
		deck = removecard(deck,deck(i))
		for j = 1:51
			flops(count,2) = deck(j)
			count = count+1
			deck = removecard(deck,deck(j))
			for k = 1:50
				flops(count,3) = deck(k)
				count = count+1
				deck = removecard(deck,deck(k))
