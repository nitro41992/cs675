$mean = 0;
$data = shift;
$dir=$data;
#$dir=$data;
for(my $i=0; $i<10; $i++){
  system("python least_squares_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > least_squares_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels least_squares_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Least Squares Error = $mean ($sd)\n";

#q^
$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python hinge_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > hinge_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels hinge_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
 
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Hinge Adaptive Error = $mean ($sd)\n";
#^if 0;
