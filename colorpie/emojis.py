# COLORPIE by Alexander Abraham
# a.k.a. "THE BLACK UNICORN".
# Licensed under the MIT license.
# This is the main module file
# for all emojis.

# This method returns a database of 66 select emojis
# in form of a map in four select categories.
def emojiPool():
  pool = {
  'grinningFace': '\U0001f600',
  'laughCry': '\U0001f602',
  'upsideDownFace': '\U0001f643',
  'heartsInFace': '\U0001f970',
  'smilingFace': '\U0001f60a',
  'haloFace': '\U0001f607',
  'winkingFace': '\U0001f609',
  'kissingFace': '\U0001f61a',
  'angryFace': '\U0001f620',
  'crazyFace': '\U0001f92a',
  'thinkingFace': '\U0001f914',
  'naughtyface': '\U0001f608',
  'seeNoEvil': '\U0001f648',
  'animalGorilla': '\U0001f98d',
  'windCloud': '\U0001f4A8',
  'sweatDroplets': '\U0001f4A6',
  'dogFace': '\U0001f436',
  'unicornHead': '\U0001f984',
  'catFace': '\U0001f431',
  'horseHead': '\U0001f434',
  'pandaFace': '\U0001f43c',
  'bearFace': '\U0001f43b',
  'tigerFace': '\U0001f42f',
  'redHeart': '\U00002764',
  'blackHeart': '\U0001f5a4',
  'backArrow': '\U0001f519',
  'soonArrow': '\U0001f51c',
  'topArrow': '\U0001f51d',
  'infinitySign': '\U000267e',
  'multiplySign': '\U00002716',
  'plusSign': '\U00002795',
  'divideSign': '\U00002797',
  'minusSign': '\U00002796',
  'tickSign': '\U00002714',
  'kitchenKnife': '\U0001f52a',
  'scissors': '\U00002702',
  'bomb': '\U0001f4a3',
  'gun': '\U0001f52b',
  'hammer': '\U0001f528',
  'wrench': '\U0001f527',
  'hammerAndWrench': '\U0001f6e0',
  'hammerAndPick': '\U00002692',
  'pick': '\U00026cf',
  'woodSaw': '\U0001fa9a',
  'axe': '\U0001fa93',
  'prideFlag': '\U0001f3f3',
  'transFlag': '\U000026a7',
  'rainbow': '\U0001f308',
  'peopleKissing': '\U0001f48f',
  'party': '\U0001f389',
  'coupleHeart': '\U0001f491',
  'sparkles': '\U00002728',
  'confetti': '\U0001f38a',
  'maleBunnies': '\U0001f46f',
  'kiss': '\U0001f48b',
  'yarn': '\U0001f9f6',
  'headPhones': '\U0001f3a7',
  'piano': '\U0001f3b9',
  'bowAndArrow': '\U0001f3f9',
  'paintBrush': '\U0001f58c',
  'paintPalette': '\U0001f3a8',
  'sewingNeedle': '\U0001faa1',
  'threadRoll': '\U0001f95f',
  'syringe': '\U0001f489',
  'pill': '\U0001f48a'
  }
  return pool

# This method returns an emoji by its name as
# a string.
def getEmoji():
  stdEmojiPool = emojiPool()
  userEmoji = stdEmojiPool[emoji]
  return userEmoji

# This method prints an emoji by its name
# to the console.
def printEmoji(emojiName):
  userEmoji = getEmoji(emojiName)
  print(userEmoji)
