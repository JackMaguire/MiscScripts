property spotPlay : «constant ****kPSP»

on run {input, parameters}
    repeat
        #delay 10
        delay 68400 #19 hours
        if application "Spotify" is running then
            tell application "Spotify" to set playerState to player state
            if playerState = spotPlay then
                tell application "Spotify" to play track "spotify:track:4CdZN5nGCellsIa7M1F5TY"
            end if
        end if
    end repeat
    return input
end run