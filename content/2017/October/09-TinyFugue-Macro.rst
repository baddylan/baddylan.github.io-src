A TinyFugue Macro!
###################

:date: 2017-10-9 10:59
:tags: information, muck, tinyfuge macro
:category: October 2017
:authors: Dylan Copeland
:summary: Tiny Fugue Macro for puppets
:status: published

So a while ago I made this thing for tf5 users that separates puppets out into
their own worlds. I've been using it for a while and I thought I might as well
share it - the code follows; to use it, stick it into your init file and type

    /puppet PuppetName puppetcommand

This will create a world called 'PuppetName', to which the contents of all lines
received from the world you typed the command into that begin with 'PuppetName>'
will be sent (excluding the 'PuppetName'.) The right angled bracket is there so
that /echo will not think you are attempting to use a nonextant option if a line
sent to the puppet begins with a dash.

When you're done with your puppet world, you can make it go away by typing:

    /kpuppet PuppetName

which redefines the defined macros to empty macros and 'disconnects' you from
the world: your connection should then behave as before.

Feel free to further modify, share, tweak, etc. (you could consider this public
domain if you wish.)

CODE BEGINS HERE * INSERT EVERYTHING BELOW THIS LINE INTO .TFRC FOR BEST RESULTS

::

        ; Macro for puppet separation
        /def puppet = \
        /let parent %; \
        /test parent := fg_world() %; \
        /addworld %{1} %; \
        /def -q -agA -m2 -t"%1>(.+)" pt_%{1} = /echo -w%1 >%%P1 %; \
        /def -w%1 -hSEND sender_%1 = /send -w%parent %2 %%* %; \
        /connect %1
        
        ; Kill a puppet
        /def kpuppet = \
        /def sender_%1= %; \
        /def pt_%1= %; \
        /dc %1

Testing.
