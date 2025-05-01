#!/bin/sh

rsync -r --exclude venv --exclude node_modules . labelpi:~/labelpi

# copy fonts

fonts="$HOME/.local/share/fonts/Adobe Caslon Pro
$HOME/.local/share/fonts/Adobe Garamond Pro
$HOME/.local/share/fonts/DIN Std
$HOME/.local/share/fonts/Helvetica Neue LT Std
$HOME/.local/share/fonts/Clarendon LT Std
$HOME/.local/share/fonts/New Century Schoolbook LT Std
/usr/share/fonts/TTF/Inconsolata-Black.ttf
/usr/share/fonts/TTF/Inconsolata-Bold.ttf
/usr/share/fonts/TTF/Inconsolata-Condensed.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedBold.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedLight.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-CondensedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-Expanded.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-ExpandedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensed.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraCondensedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpanded.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedLight.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraExpandedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-ExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-Light.ttf
/usr/share/fonts/TTF/Inconsolata-Medium.ttf
/usr/share/fonts/TTF/Inconsolata-Regular.ttf
/usr/share/fonts/TTF/Inconsolata-SemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensed.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedLight.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-SemiCondensedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpanded.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedLight.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-SemiExpandedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensed.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedLight.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-UltraCondensedSemiBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpanded.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedBlack.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedExtraBold.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedExtraLight.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedLight.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedMedium.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedRegular.ttf
/usr/share/fonts/TTF/Inconsolata-UltraExpandedSemiBold.ttf"


rsync -r ~/.local/share/fonts/din-round-pro labelpi:~/.local/share/fonts


# sync fonts
printf "$fonts" | while read font; do
    echo "Syncing $font"
    rsync -r "$font" labelpi:~/.local/share/fonts
done

