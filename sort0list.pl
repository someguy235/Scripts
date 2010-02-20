#!/usr/bin/perl
#
#Sorts an exported iTunes playlist

open(OUT, ">0sorted.txt") or die ("Unable to open out file");
open(IN, "0.txt") or die ("Unable to open file");

@data = <IN>;
@lines = ();
@artistArray = ();
@albumArray=();
$init =0;
$outputInit=0;
$artistTime=0;
$albumTime=0;
$totalTime=0;
$tracks=0;
$artists=0;
foreach $line (@data){
	@splitLine = split(/\t/, $line);
	if ($init == 0){
		$currentArtist=$splitLine[5];
		$init=1;
	}else{
		$albumtime=0;
		if (lc $splitLine[5] ne lc $currentArtist){
			if($init ==1){$init=2}
			else{output();}
		}
		$artistTime+=$splitLine[7];
		$totalTime+=$splitLine[7];
		$tracks++;
		push @artistArray, [@splitLine];
		$currentArtist = $splitLine[5];
	}
}
output();
printf OUT "Artists: $artists\tTracks: $tracks\t Time: %s", getTime($totalTime);
close(OUT);
close(IN);

sub output{
	$artists++;
	@artistArray = sort{
		$a->[3] cmp $b->[3] || $a->[10] <=> $b->[10]
	}@artistArray;
	printf OUT "$currentArtist (%s)\n", getTime($artistTime);
	$albumName = $artistArray[0]->[3];
	foreach $song (@artistArray){
		if (lc @$song[3] ne lc $albumName){
			albumOutput();
		}
		push @albumArray, [@$song];
		$albumTime+=@$song[7];
		$albumName=@$song[3];
	}
	albumOutput();
	$artistTime=0;
	@artistArray=();
}
sub albumOutput{
	printf OUT "\t$albumName (%s)\n", getTime($albumTime);
	$albumTime=0;
	foreach $albumSong (@albumArray){
		printf OUT "\t\t@$albumSong[10]\t%s\t@$albumSong[0]\n", getTime(@$albumSong[7]);
	}
	@albumArray=();
}
sub getTime{
	$seconds = $_[0]%60;
	$minutes = (($_[0]-$seconds)%3600)/60;
	$hours = ($_[0]-(($minutes*60)+$seconds))/3600;
	if ($hours == 0){
		$return = sprintf("%2d:%02d", $minutes, $seconds);
	}else{
		$return = sprintf("$hours:%02d:%02d", $minutes, $seconds);
	}
}
