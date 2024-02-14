if status is-interactive
    # Commands to run in interactive sessions can go here

    alias cls="clear"
    alias .!="source ~/.config/fish/config.fish"
    alias ls="exa -1 -l -a -h --no-filesize --no-time --icons --color=always --color-scale"



    function starship_transient_prompt_func
        starship prompt --profile short
    end
    starship init fish | source
    enable_transience



end
