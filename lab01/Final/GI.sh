
out='GI.png'
gnuplot << PLOTTHIS
set term postscript eps enhanced color  "Helvetica" 32

set terminal png
set output "${out}"
set autoscale
unset log
unset label
set grid 
set title "Genuine Score Vs Imposter Score Frequency Histogram"
set key right top

#set ylabel "Frequency (%)"
#set xlabel "Score (%)"
#set format x "10^{%L}"

##########################
#set xrange [9100:9500]
#set yrange [0:0.8]
#########################

# set logscale x
set xrange [0:1000000]
set yrange [0:1000]
# set xtics [0:1]
#set xtics (0.2,0.25,0.5,0.75,1)

#set xlabel "Threshold"
#set ylabel "FAR/FRR (%)"

set xlabel "Score"
set ylabel "Frequency"

##############################################################

# plot	"findTrreshold.out" using 2:1 title 'Zzz' w linespoints
plot	"I_HIST" using 1:2 title 'Imposter' w linespoints, \
		"G_HIST" using 1:2 title 'Genuine' w linespoints, \

##############################################################

##############################################################
pause mouse
PLOTTHIS

