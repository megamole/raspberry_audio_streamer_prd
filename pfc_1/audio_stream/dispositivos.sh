aplay -l | grep tarjeta | awk  '{print "hw:"$2  $8}' | rev | cut -c 2- | rev |sed 's/\(.*\):/\1,/' >dispositivos_audio
