import discord
import json
import asyncio
from discord import app_commands
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

with open('roles_membres.json', 'r', encoding='utf-8') as file:
    roles_data = json.load(file)

# Fonction pour vérifier si l'utilisateur a le rôle "Manager Minecraft"
async def has_manager_minecraft_role(interaction: discord.Interaction):
    return any(role.name == "Manager Minecraft" for role in interaction.user.roles)
# Dictionnaire d'autocomplétion Minecraft
MINECRAFT_PLAYERS = ["@a", "@p", "@r", "@s", "@e"]
ENTITIES = [
    "minecraft:armor_stand",
    "minecraft:axolotl",
    "minecraft:bat",
    "minecraft:bee",
    "minecraft:blaze",
    "minecraft:cat",
    "minecraft:cave_spider",
    "minecraft:chicken",
    "minecraft:cod",
    "minecraft:cow",
    "minecraft:creeper",
    "minecraft:dolphin",
    "minecraft:donkey",
    "minecraft:drowned",
    "minecraft:elder_guardian",
    "minecraft:enderman",
    "minecraft:endermite",
    "minecraft:evoker",
    "minecraft:fox",
    "minecraft:ghast",
    "minecraft:giant",
    "minecraft:glow_squid",
    "minecraft:goat",
    "minecraft:guardian",
    "minecraft:hoglin",
    "minecraft:horse",
    "minecraft:husk",
    "minecraft:illusioner",
    "minecraft:iron_golem",
    "minecraft:llama",
    "minecraft:magma_cube",
    "minecraft:mooshroom",
    "minecraft:mule",
    "minecraft:ocelot",
    "minecraft:panda",
    "minecraft:parrot",
    "minecraft:phantom",
    "minecraft:pig",
    "minecraft:piglin",
    "minecraft:pillager",
    "minecraft:polar_bear",
    "minecraft:pufferfish",
    "minecraft:rabbit",
    "minecraft:ravager",
    "minecraft:salmon",
    "minecraft:sheep",
    "minecraft:shulker",
    "minecraft:silverfish",
    "minecraft:skeleton",
    "minecraft:skeleton_horse",
    "minecraft:slime",
    "minecraft:snow_golem",
    "minecraft:spider",
    "minecraft:squid",
    "minecraft:stray",
    "minecraft:strider",
    "minecraft:tropical_fish",
    "minecraft:turtle",
    "minecraft:vex",
    "minecraft:villager",
    "minecraft:vindicator",
    "minecraft:wandering_trader",
    "minecraft:witch",
    "minecraft:wither",
    "minecraft:wither_skeleton",
    "minecraft:wolf",
    "minecraft:zombie",
    "minecraft:zombie_horse",
    "minecraft:zombie_villager",
    "minecraft:zombified_piglin"
]

ENTITY_MODIFIERS = [
    "type=", "distance=", "name=", "limit=", "sort=", "scores=", "team=", "tag="
]
ITEMS = [
    "minecraft:acacia_boat",
    "minecraft:acacia_button",
    "minecraft:acacia_door",
    "minecraft:acacia_fence",
    "minecraft:acacia_fence_gate",
    "minecraft:acacia_hanging_sign",
    "minecraft:acacia_leaves",
    "minecraft:acacia_log",
    "minecraft:acacia_planks",
    "minecraft:acacia_pressure_plate",
    "minecraft:acacia_sapling",
    "minecraft:acacia_sign",
    "minecraft:acacia_slab",
    "minecraft:acacia_stairs",
    "minecraft:acacia_trapdoor",
    "minecraft:acacia_wood",
    "minecraft:activator_rail",
    "minecraft:allium",
    "minecraft:amethyst_block",
    "minecraft:amethyst_cluster",
    "minecraft:ancient_debris",
    "minecraft:andesite",
    "minecraft:andesite_slab",
    "minecraft:andesite_stairs",
    "minecraft:andesite_wall",
    "minecraft:anvil",
    "minecraft:apple",
    "minecraft:armor_stand",
    "minecraft:arrow",
    "minecraft:axolotl_bucket",
    "minecraft:azalea",
    "minecraft:azalea_leaves",
    "minecraft:azalea_leaves", "minecraft:azur_spray", "minecraft:bat_spawn_egg", "minecraft:beacon", 
    "minecraft:beehive", "minecraft:bees", "minecraft:beetroot", "minecraft:beetroot_seeds", 
    "minecraft:beetroot_soup", "minecraft:bell", "minecraft:birch_boat", "minecraft:birch_button", 
    "minecraft:birch_door", "minecraft:birch_fence", "minecraft:birch_fence_gate", "minecraft:birch_hanging_sign", 
    "minecraft:birch_leaves", "minecraft:birch_log", "minecraft:birch_planks", "minecraft:birch_pressure_plate", 
    "minecraft:birch_sapling", "minecraft:birch_sign", "minecraft:birch_slab", "minecraft:birch_stairs", 
    "minecraft:birch_trapdoor", "minecraft:birch_wood", "minecraft:blast_furnace", "minecraft:blaze_powder", 
    "minecraft:blaze_rod", "minecraft:blaze_spawn_egg", "minecraft:blue_dye", "minecraft:blue_orchid", 
    "minecraft:bone", "minecraft:bone_block", "minecraft:bone_meal", "minecraft:book", "minecraft:bookshelf", 
    "minecraft:bow", "minecraft:bow_arrow", "minecraft:bricks", "minecraft:brown_mushroom", "minecraft:brown_mushroom_block",
    "minecraft:bucket", "minecraft:calf_spawn_egg", "minecraft:carved_pumpkin", "minecraft:cauldron", 
    "minecraft:chain", "minecraft:chiseled_bookshelf", "minecraft:chiseled_quartz_block", "minecraft:chest", 
    "minecraft:chiseled_stone_bricks", "minecraft:clay_ball", "minecraft:coal_block", "minecraft:coal_ore",
    "minecraft:cobblestone", "minecraft:cobblestone_slab", "minecraft:cobblestone_stairs", "minecraft:cobblestone_wall",
    "minecraft:composter", "minecraft:conduit", "minecraft:copper_block", "minecraft:copper_ore", "minecraft:crafting_table",
    "minecraft:creeper_spawn_egg", "minecraft:crossbow", "minecraft:cut_sandstone", "minecraft:cut_sandstone_slab", "minecraft:cyan_dye",
    "minecraft:cyan_glazed_terracotta", "minecraft:dark_oak_boat", "minecraft:dark_oak_button", "minecraft:dark_oak_door",
    "minecraft:dark_oak_fence", "minecraft:dark_oak_fence_gate", "minecraft:dark_oak_hanging_sign", 
    "minecraft:dark_oak_leaves", "minecraft:dark_oak_log", "minecraft:dark_oak_planks", "minecraft:dark_oak_pressure_plate", 
    "minecraft:dark_oak_sapling", "minecraft:dark_oak_sign", "minecraft:dark_oak_slab", "minecraft:dark_oak_stairs", 
    "minecraft:dark_oak_trapdoor", "minecraft:dark_oak_wood", "minecraft:daylight_detector", "minecraft:dead_bush", 
    "minecraft:detector_rail", "minecraft:diamond", "minecraft:diamond_axe", "minecraft:diamond_block", "minecraft:diamond_boots", 
    "minecraft:diamond_chestplate", "minecraft:diamond_helmet", "minecraft:diamond_hoe", "minecraft:diamond_horse_armor", 
    "minecraft:diamond_leggings", "minecraft:diamond_pickaxe", "minecraft:diamond_shovel", "minecraft:diamond_sword", 
    "minecraft:diamond_sword", "minecraft:diorite", "minecraft:diorite_slab", "minecraft:diorite_stairs", "minecraft:diorite_wall", 
    "minecraft:dispenser", "minecraft:diamond_block", "minecraft:dropped_item", "minecraft:dripstone_block", "minecraft:drowned_spawn_egg", 
    "minecraft:ender_pearl", "minecraft:end_crystal", "minecraft:end_rod", "minecraft:end_stone", "minecraft:end_stone_brick_slab", 
    "minecraft:end_stone_brick_stairs", "minecraft:end_stone_brick_wall", "minecraft:end_stone_slab", "minecraft:end_stone_stairs",
    "minecraft:enderman_spawn_egg", "minecraft:endstone", "minecraft:experience_bottle", "minecraft:farmland", "minecraft:feather", "minecraft:fern", "minecraft:filled_map", 
    "minecraft:fire_charge", "minecraft:fire_coral", "minecraft:fire_coral_block", "minecraft:fire_coral_fan", 
    "minecraft:firework_rocket", "minecraft:firework_star", "minecraft:fish_bucket", "minecraft:flint", 
    "minecraft:flint_and_steel", "minecraft:flower_pot", "minecraft:flowering_azalea", "minecraft:flowering_azalea_leaves", 
    "minecraft:furnace", "minecraft:ghast_spawn_egg", "minecraft:glass", "minecraft:glow_ink_sac", "minecraft:glow_item_frame", 
    "minecraft:glow_lichen", "minecraft:glowstone", "minecraft:gold_block", "minecraft:gold_ore", "minecraft:golden_apple", 
    "minecraft:golden_axe", "minecraft:golden_boots", "minecraft:golden_carrot", "minecraft:golden_chestplate", 
    "minecraft:golden_helmet", "minecraft:golden_hoe", "minecraft:golden_leggings", "minecraft:golden_pickaxe", 
    "minecraft:golden_shovel", "minecraft:golden_sword", "minecraft:granite", "minecraft:granite_slab", 
    "minecraft:granite_stairs", "minecraft:granite_wall", "minecraft:grass", "minecraft:grass_block", "minecraft:grass_path",
    "minecraft:gray_dye", "minecraft:gray_glazed_terracotta", "minecraft:green_dye", "minecraft:green_glazed_terracotta", 
    "minecraft:grindstone", "minecraft:hanging_sign", "minecraft:hopper", "minecraft:hopper_minecart", "minecraft:horn_coral",
    "minecraft:horn_coral_block", "minecraft:horn_coral_fan", "minecraft:iron_bars", "minecraft:iron_block", "minecraft:iron_door", "minecraft:iron_hoe", "minecraft:iron_horse_armor",
    "minecraft:iron_ingot", "minecraft:iron_leggings", "minecraft:iron_nugget", "minecraft:iron_ore", "minecraft:iron_pickaxe",
    "minecraft:iron_shovel", "minecraft:iron_sword", "minecraft:iron_trapdoor", "minecraft:item_frame", "minecraft:jack_o_lantern",
    "minecraft:jungle_boat", "minecraft:jungle_button", "minecraft:jungle_door", "minecraft:jungle_fence", "minecraft:jungle_fence_gate",
    "minecraft:jungle_hanging_sign", "minecraft:jungle_leaves", "minecraft:jungle_log", "minecraft:jungle_planks", "minecraft:jungle_pressure_plate",
    "minecraft:jungle_sapling", "minecraft:jungle_sign", "minecraft:jungle_slab", "minecraft:jungle_stairs", "minecraft:jungle_trapdoor",
    "minecraft:jungle_wood", "minecraft:kelp", "minecraft:kelp_block", "minecraft:ladder", "minecraft:lava_bucket", 
    "minecraft:lava_coral", "minecraft:lava_coral_block", "minecraft:lava_coral_fan", "minecraft:lead", "minecraft:leather",
    "minecraft:leather_boots", "minecraft:leather_chestplate", "minecraft:leather_helmet", "minecraft:leather_leggings", "minecraft:leather_helmet",
    "minecraft:light_blue_dye", "minecraft:light_blue_glazed_terracotta", "minecraft:light_gray_dye", "minecraft:light_gray_glazed_terracotta",
    "minecraft:light_weighted_pressure_plate", "minecraft:lightning_rod", "minecraft:lime_dye", "minecraft:lime_glazed_terracotta",
    "minecraft:lodestone", "minecraft:loom", "minecraft:magenta_dye", "minecraft:magenta_glazed_terracotta", "minecraft:map",
    "minecraft:melons", "minecraft:melon", "minecraft:melon_block", "minecraft:mob_spawner", "minecraft:minecart", "minecraft:minecart_with_chest", "minecraft:minecart_with_command_block",
    "minecraft:minecart_with_furnace", "minecraft:minecart_with_hopper", "minecraft:mob_spawn_egg", "minecraft:melon_seeds",
    "minecraft:melon_slice", "minecraft:music_disc_11", "minecraft:music_disc_13", "minecraft:music_disc_blocks",
    "minecraft:music_disc_cat", "minecraft:music_disc_chirp", "minecraft:music_disc_far", "minecraft:music_disc_mall",
    "minecraft:music_disc_mellohi", "minecraft:music_disc_pigstep", "minecraft:music_disc_stal", "minecraft:music_disc_strad",
    "minecraft:music_disc_wait", "minecraft:music_disc_ward", "minecraft:nether_brick", "minecraft:nether_brick_slab",
    "minecraft:nether_brick_stairs", "minecraft:nether_brick_wall", "minecraft:nether_quartz_ore", "minecraft:nether_star",
    "minecraft:nether_wart", "minecraft:nether_wart_block", "minecraft:netherite_axe", "minecraft:netherite_block",
    "minecraft:netherite_boots", "minecraft:netherite_chestplate", "minecraft:netherite_helmet", "minecraft:netherite_ingot",
    "minecraft:netherite_leggings", "minecraft:netherite_pickaxe", "minecraft:netherite_shovel", "minecraft:netherite_sword",
    "minecraft:note_block", "minecraft:oak_boat", "minecraft:oak_button", "minecraft:oak_door", "minecraft:oak_fence",
    "minecraft:oak_fence_gate", "minecraft:oak_hanging_sign", "minecraft:oak_leaves", "minecraft:oak_log", "minecraft:oak_planks",
    "minecraft:oak_pressure_plate", "minecraft:oak_sapling", "minecraft:oak_sign", "minecraft:oak_slab", "minecraft:oak_stairs",
    "minecraft:oak_trapdoor", "minecraft:oak_wood", "minecraft:observer", "minecraft:ocelot_spawn_egg", "minecraft:orange_dye",
    "minecraft:orange_glazed_terracotta", "minecraft:orange_tulip", "minecraft:oxeye_daisy", "minecraft:packed_ice",
    "minecraft:painted_glass", "minecraft:painted_glass_pane", "minecraft:paper", "minecraft:parrot_spawn_egg", 
    "minecraft:peony", "minecraft:piston", "minecraft:player_head", "minecraft:poppy", "minecraft:potato",
    "minecraft:potatoes", "minecraft:powered_rail", "minecraft:prismarine", "minecraft:prismarine_brick_slab", 
    "minecraft:prismarine_brick_stairs", "minecraft:prismarine_brick_wall", "minecraft:prismarine_crystals", 
    "minecraft:prismarine_slab", "minecraft:prismarine_stairs", "minecraft:prismarine_wall", "minecraft:pumpkin", 
    "minecraft:pumpkin_seeds", "minecraft:pumpkin_stem", "minecraft:purpur_block", "minecraft:purpur_pillar", 
    "minecraft:purpur_slab", "minecraft:purpur_stairs", "minecraft:purpur_wall", "minecraft:quartz_block", 
    "minecraft:quartz_brick_slab", "minecraft:quartz_brick_stairs", "minecraft:quartz_block_slab", "minecraft:quartz_slab",
    "minecraft:quartz_stairs", "minecraft:quartz_wall", "minecraft:rabbit", "minecraft:rabbit_foot", "minecraft:rabbit_hide",
    "minecraft:rabbit_spawn_egg", "minecraft:rail", "minecraft:red_dye", "minecraft:red_glazed_terracotta", 
    "minecraft:red_mushroom", "minecraft:red_mushroom_block", "minecraft:red_nether_brick_slab", 
    "minecraft:red_nether_brick_stairs", "minecraft:red_nether_brick_wall", "minecraft:redstone", "minecraft:redstone_block",
    "minecraft:redstone_lamp", "minecraft:redstone_torch", "minecraft:repeater", "minecraft:repeating_command_block", 
    "minecraft:rose_bush", "minecraft:roses", "minecraft:rouge_dye", "minecraft:saddle", "minecraft:sand", "minecraft:sandstone",
    "minecraft:sandstone_slab", "minecraft:sandstone_stairs", "minecraft:sandstone_wall", "minecraft:sapling", 
    "minecraft:sea_lantern", "minecraft:sea_pickle", "minecraft:seeds", "minecraft:shears", "minecraft:skeleton_spawn_egg", 
    "minecraft:skull", "minecraft:slime_ball", "minecraft:slime_spawn_egg", "minecraft:slime_block", "minecraft:small_amethyst_bud", 
    "minecraft:small_dripleaf", "minecraft:smithing_table", "minecraft:smooth_basalt", "minecraft:smooth_blackstone", 
    "minecraft:smooth_blackstone_slab", "minecraft:smooth_blackstone_stairs", "minecraft:smooth_brick_slab", 
    "minecraft:smooth_brick_stairs", "minecraft:smooth_cobblestone", "minecraft:smooth_cobblestone_slab", 
    "minecraft:smooth_cobblestone_stairs", "minecraft:smooth_stone", "minecraft:smooth_stone_slab", "minecraft:smooth_stone_stairs",
    "minecraft:snow", "minecraft:snow_block", "minecraft:snowball", "minecraft:soapstone", "minecraft:spawner",
    "minecraft:spectator_spawn_egg", "minecraft:splash_potion", "minecraft:sponge", "minecraft:spruce_boat", 
    "minecraft:spruce_button", "minecraft:spruce_door", "minecraft:spruce_fence", "minecraft:spruce_fence_gate", 
    "minecraft:spruce_hanging_sign", "minecraft:spruce_leaves", "minecraft:spruce_log", "minecraft:spruce_planks", 
    "minecraft:spruce_pressure_plate", "minecraft:spruce_sapling", "minecraft:spruce_sign", "minecraft:spruce_slab",
    "minecraft:spruce_stairs", "minecraft:spruce_trapdoor", "minecraft:spruce_wood", "minecraft:sticky_piston", 
    "minecraft:stone", "minecraft:stone_brick", "minecraft:stone_brick_slab", "minecraft:stone_brick_stairs", 
    "minecraft:stone_brick_wall", "minecraft:stone_button", "minecraft:stone_hoe", "minecraft:stone_pickaxe", 
    "minecraft:stone_pressure_plate", "minecraft:stone_shovel", "minecraft:stone_slab", "minecraft:stone_stairs", 
    "minecraft:stone_sword", "minecraft:stonecutter", "minecraft:stonecutting_table", "minecraft:stripped_acacia_log", 
    "minecraft:stripped_birch_log", "minecraft:stripped_crimson_hyphae", "minecraft:stripped_dark_oak_log", 
    "minecraft:stripped_jungle_log", "minecraft:stripped_oak_log", "minecraft:stripped_spruce_log", "minecraft:sugar_cane", 
    "minecraft:sunflower", "minecraft:suspicious_stew", "minecraft:sweet_berries", "minecraft:sweet_berry_bush", 
    "minecraft:tag", "minecraft:target", "minecraft:terracotta", "minecraft:trident", "minecraft:tripwire", 
    "minecraft:tripwire_hook", "minecraft:tropical_fish", "minecraft:tropical_fish_bucket", "minecraft:turtle_egg", 
    "minecraft:turtle_helmet", "minecraft:acacia_planks", "minecraft:acacia_sign", "minecraft:acacia_stairs", "minecraft:acacia_trapdoor", "minecraft:acacia_wood", "minecraft:observer", "minecraft:oak_boat", "minecraft:oak_button", 
    "minecraft:oak_door", "minecraft:oak_fence", "minecraft:oak_fence_gate", "minecraft:oak_hanging_sign", 
    "minecraft:oak_leaves", "minecraft:oak_log", "minecraft:oak_planks", "minecraft:oak_pressure_plate", 
    "minecraft:oak_sapling", "minecraft:oak_sign", "minecraft:oak_slab", "minecraft:oak_stairs", 
    "minecraft:oak_trapdoor", "minecraft:oak_wood", "minecraft:observer", "minecraft:ocelot_spawn_egg", 
    "minecraft:orange_dye", "minecraft:orange_glazed_terracotta", "minecraft:orange_tulip", "minecraft:oxeye_daisy", 
    "minecraft:packed_ice", "minecraft:painted_glass", "minecraft:painted_glass_pane", "minecraft:paper", 
    "minecraft:parrot_spawn_egg", "minecraft:peony", "minecraft:piston", "minecraft:player_head", 
    "minecraft:poppy", "minecraft:potato", "minecraft:potatoes", "minecraft:powered_rail", "minecraft:prismarine", 
    "minecraft:prismarine_brick_slab", "minecraft:prismarine_brick_stairs", "minecraft:prismarine_brick_wall", 
    "minecraft:prismarine_crystals", "minecraft:prismarine_slab", "minecraft:prismarine_stairs", "minecraft:prismarine_wall", 
    "minecraft:pumpkin", "minecraft:pumpkin_seeds", "minecraft:pumpkin_stem", "minecraft:purpur_block", 
    "minecraft:purpur_pillar", "minecraft:purpur_slab", "minecraft:purpur_stairs", "minecraft:purpur_wall", 
    "minecraft:quartz_block", "minecraft:quartz_brick_slab", "minecraft:quartz_brick_stairs", "minecraft:quartz_block_slab", 
    "minecraft:quartz_slab", "minecraft:quartz_stairs", "minecraft:quartz_wall", "minecraft:rabbit", 
    "minecraft:rabbit_foot", "minecraft:rabbit_hide", "minecraft:rabbit_spawn_egg", "minecraft:rail", 
    "minecraft:red_dye", "minecraft:red_glazed_terracotta", "minecraft:red_mushroom", "minecraft:red_mushroom_block", "minecraft:rose_bush", "minecraft:rotten_flesh", "minecraft:saddle", "minecraft:sand", "minecraft:sandstone", 
    "minecraft:sandstone_slab", "minecraft:sandstone_stairs", "minecraft:sandstone_wall", "minecraft:sapling", 
    "minecraft:sea_lantern", "minecraft:sea_pickle", "minecraft:seeds", "minecraft:shears", "minecraft:skeleton_spawn_egg", 
    "minecraft:skull", "minecraft:slime_ball", "minecraft:slime_spawn_egg", "minecraft:slime_block", "minecraft:small_amethyst_bud", 
    "minecraft:small_dripleaf", "minecraft:smithing_table", "minecraft:smooth_basalt", "minecraft:smooth_blackstone", 
    "minecraft:smooth_blackstone_slab", "minecraft:smooth_blackstone_stairs", "minecraft:smooth_brick_slab", 
    "minecraft:smooth_brick_stairs", "minecraft:smooth_cobblestone", "minecraft:smooth_cobblestone_slab", 
    "minecraft:smooth_cobblestone_stairs", "minecraft:smooth_stone", "minecraft:smooth_stone_slab", "minecraft:smooth_stone_stairs",
    "minecraft:snow", "minecraft:snow_block", "minecraft:snowball", "minecraft:soapstone", "minecraft:spawner",
    "minecraft:spectator_spawn_egg", "minecraft:splash_potion", "minecraft:sponge", "minecraft:spruce_boat", 
    "minecraft:spruce_button", "minecraft:spruce_door", "minecraft:spruce_fence", "minecraft:spruce_fence_gate", 
    "minecraft:spruce_hanging_sign", "minecraft:spruce_leaves", "minecraft:spruce_log", "minecraft:spruce_planks", 
    "minecraft:spruce_pressure_plate", "minecraft:spruce_sapling", "minecraft:spruce_sign", "minecraft:spruce_slab", "minecraft:spruce_stairs", "minecraft:spruce_trapdoor", "minecraft:spruce_wood", "minecraft:sticky_piston", 
    "minecraft:stone", "minecraft:stone_brick", "minecraft:stone_brick_slab", "minecraft:stone_brick_stairs", 
    "minecraft:stone_brick_wall", "minecraft:stone_button", "minecraft:stone_hoe", "minecraft:stone_pickaxe", 
    "minecraft:stone_pressure_plate", "minecraft:stone_shovel", "minecraft:stone_slab", "minecraft:stone_stairs", 
    "minecraft:stone_sword", "minecraft:stonecutter", "minecraft:stonecutting_table", "minecraft:stripped_acacia_log", 
    "minecraft:stripped_birch_log", "minecraft:stripped_crimson_hyphae", "minecraft:stripped_dark_oak_log", 
    "minecraft:stripped_jungle_log", "minecraft:stripped_oak_log", "minecraft:stripped_spruce_log", "minecraft:sugar_cane", 
    "minecraft:sunflower", "minecraft:suspicious_stew", "minecraft:sweet_berries", "minecraft:sweet_berry_bush", 
    "minecraft:tag", "minecraft:target", "minecraft:terracotta", "minecraft:trident", "minecraft:tripwire", 
    "minecraft:tripwire_hook", "minecraft:tropical_fish", "minecraft:tropical_fish_bucket", "minecraft:turtle_egg", 
    "minecraft:turtle_helmet", "minecraft:acacia_planks", "minecraft:acacia_sign", "minecraft:acacia_stairs", "minecraft:acacia_trapdoor", "minecraft:warped_planks", "minecraft:warped_sign", "minecraft:warped_slab", "minecraft:warped_stairs", 
    "minecraft:warped_trapdoor", "minecraft:warped_wood", "minecraft:wheat", "minecraft:wheat_seeds", "minecraft:wet_sponge", 
    "minecraft:whiterun", "minecraft:wooden_button", "minecraft:wooden_slab", "minecraft:wool", "minecraft:worn_shulker_box", 
    "minecraft:zombie_spawn_egg", "minecraft:yellow_dye", "minecraft:yellow_glazed_terracotta", "minecraft:yellow_tulip", 
    "minecraft:zombified_piglin_spawn_egg", "minecraft:stone_slab", "minecraft:stone_stairs", "minecraft:nether_brick_slab"
]


NBT_TAGS = [
    "CustomName", "Enchantments", "Unbreakable", "Lore", "HideFlags", "AttributeModifiers"
]
NBT_VALUES = {
    "CustomName": '{CustomName:"\\"Nom personnalisé\\""}',
    "Lore": '{display:{Lore:["\\"Première ligne de description\\"","\\"Deuxième ligne\\""]}}',
    "Unbreakable": "{Unbreakable:1b}",
    "HideFlags": "{HideFlags:63}",
    "Damage": "{Damage:0}",
    "RepairCost": "{RepairCost:2}",
    "CustomModelData": "{CustomModelData:12345}",

    # Enchantements
    "Enchantments": '{Enchantments:[{id:"minecraft:sharpness",lvl:5s},{id:"minecraft:unbreaking",lvl:3s}]}',
    "StoredEnchantments": '{StoredEnchantments:[{id:"minecraft:fortune",lvl:2s}]}',
    
    # Potions et effets
    "Potion": '{Potion:"minecraft:strength"}',
    "CustomPotionEffects": '{CustomPotionEffects:[{Id:1,Amplifier:2,Duration:600}]}',

    # Modificateurs d'attributs
    "AttributeModifiers": '{AttributeModifiers:[{AttributeName:"generic.max_health",Amount:10,Operation:0,Slot:"mainhand",UUID:[I;1,2,3,4]}]}',
    
    # Conteneurs et blocs
    "BlockEntityTag": '{BlockEntityTag:{Items:[{Slot:0,id:"minecraft:diamond",Count:64b}]}}',
    "Items": '{Items:[{Slot:0b,id:"minecraft:diamond",Count:64b},{Slot:1b,id:"minecraft:golden_apple",Count:16b}]}',

    # Effets sur la tête de joueur
    "SkullOwner": '{SkullOwner:{Id:"uuid",Name:"PlayerName"}}',

    # Tag générique
    "Tags": '{Tags:["tag1","tag2"]}'
}

# Liste des enchantements (utilisés dans l'autocomplétion pour Enchantments)
ENCHANTMENTS = [
    # Enchantements universels
    "minecraft:mending",
    "minecraft:unbreaking",
    "minecraft:vanishing_curse",

    # Armes de mêlée (épées et haches)
    "minecraft:bane_of_arthropods",
    "minecraft:fire_aspect",
    "minecraft:knockback",
    "minecraft:looting",
    "minecraft:sharpness",
    "minecraft:smite",
    "minecraft:sweeping_edge",

    # Armes à distance (arcs et arbalètes)
    "minecraft:flame",
    "minecraft:infinity",
    "minecraft:power",
    "minecraft:punch",
    "minecraft:multishot",
    "minecraft:piercing",
    "minecraft:quick_charge",

    # Tridents
    "minecraft:channeling",
    "minecraft:impaling",
    "minecraft:loyalty",
    "minecraft:riptide",

    # Outils (pelles, pioches, haches)
    "minecraft:efficiency",
    "minecraft:fortune",
    "minecraft:silk_touch",

    # Armures
    "minecraft:aqua_affinity",
    "minecraft:blast_protection",
    "minecraft:depth_strider",
    "minecraft:feather_falling",
    "minecraft:fire_protection",
    "minecraft:frost_walker",
    "minecraft:protection",
    "minecraft:projectile_protection",
    "minecraft:respiration",
    "minecraft:soul_speed",
    "minecraft:thorns",
    "minecraft:binding_curse",

    # Canne à pêche
    "minecraft:luck_of_the_sea",
    "minecraft:lure"
]
EFFECTS = [
    "minecraft:absorption",
    "minecraft:bad_omen",
    "minecraft:blindness",
    "minecraft:conduit_power",
    "minecraft:darkness",
    "minecraft:dolphins_grace",
    "minecraft:fire_resistance",
    "minecraft:glowing",
    "minecraft:haste",
    "minecraft:health_boost",
    "minecraft:hero_of_the_village",
    "minecraft:hunger",
    "minecraft:instant_health",
    "minecraft:instant_damage",
    "minecraft:invisibility",
    "minecraft:jump_boost",
    "minecraft:levitation",
    "minecraft:luck",
    "minecraft:mining_fatigue",
    "minecraft:nausea",
    "minecraft:night_vision",
    "minecraft:poison",
    "minecraft:regeneration",
    "minecraft:resistance",
    "minecraft:saturation",
    "minecraft:slowness",
    "minecraft:speed",
    "minecraft:strength",
    "minecraft:unluck",
    "minecraft:water_breathing",
    "minecraft:weakness",
    "minecraft:wither"
]


async def autocomplete_player(interaction: discord.Interaction, current: str):
    # Si le préfixe est "@e", c'est un sélecteur d'entité, on gère les entités
    if current.startswith("@e["):
        if "=" in current:
            if "type=" in current:
                entity_current = current.split("type=")[-1].replace("]", "")
                return [
                    app_commands.Choice(name=entity, value=f"@e[type={entity}]")
                    for entity in ENTITIES
                    if entity.startswith(entity_current)
                ]
        else:
            mod_current = current[3:]
            return [
                app_commands.Choice(name=f"@e[{mod}", value=f"@e[{mod}")
                for mod in ENTITY_MODIFIERS
                if mod.startswith(mod_current)
            ]
    # Si le préfixe est "@a", c'est pour tous les joueurs
    elif current.startswith("@a"):
        return [app_commands.Choice(name="@a", value="@a")]
    # Autocomplétion des joueurs
    else:
        return [
            app_commands.Choice(name=player, value=player)
            for player in roles_data.keys()
            if current.lower() in player.lower()
        ]
    
async def autocomplete_item(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=item, value=item)
        for item in ITEMS
        if current.lower() in item.lower()
    ]

async def autocomplete_nbt(interaction: discord.Interaction, current: str):
    if ":" not in current:
        return [
            app_commands.Choice(name=tag, value=tag)
            for tag in NBT_TAGS
            if current.lower() in tag.lower()
        ]
    else:
        tag, value = current.split(":", 1)  # Séparer uniquement sur le premier ":"
        if tag == "Enchantments":
            # Extraire la partie après "[{id:...}"
            partial_enchantment = value.split("{id:")[-1].replace("}", "").strip()
            return [
                app_commands.Choice(
                    name=f"{enchantment} (lvl:1-5)",
                    value=f'{tag}:[{{id:"{enchantment}",lvl:1}}]'
                )
                for enchantment in ENCHANTMENTS
                if partial_enchantment.lower() in enchantment.lower()
            ]
        return []

@tree.command(name="give", description="Commande Minecraft /give avec autocomplétion avancée")
@app_commands.describe(player="Sélectionnez le joueur ou l'entité")
@app_commands.autocomplete(player=autocomplete_player)
@app_commands.describe(item="Sélectionnez l'item à donner")
@app_commands.autocomplete(item=autocomplete_item)
@app_commands.describe(nbt="Ajoutez un NBT pour l'item (facultatif)")
@app_commands.autocomplete(nbt=autocomplete_nbt)
async def give_command(interaction: discord.Interaction, player: str, item: str, amount: int = 1, nbt: str = None):
    command = f"/give {player} {item} {amount}"
    if nbt:
        command += f" {nbt}"
    await interaction.response.send_message(command)



async def autocomplete_enchantment(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=enchantment, value=enchantment)
        for enchantment in ENCHANTMENTS
        if current.lower() in enchantment.lower()
    ]

@tree.command(name="enchant", description="Commande Minecraft /enchant avec autocomplétion avancée")
@app_commands.describe(player="Sélectionnez le joueur ou l'entité")
@app_commands.autocomplete(player=autocomplete_player)
@app_commands.describe(enchantment="Sélectionnez l'enchantement à appliquer")
@app_commands.autocomplete(enchantment=autocomplete_enchantment)
@app_commands.describe(level="Niveau de l'enchantement (1-5)")
async def enchant_command(interaction: discord.Interaction, player: str, enchantment: str, level: int = 1):
    level = max(1, min(level, 5))  # Limite le niveau entre 1 et 5
    command = f"/enchant {player} {enchantment} {level}"
    await interaction.response.send_message(command)

async def autocomplete_entity(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=entity, value=entity)
        for entity in ENTITIES
        if current.lower() in entity.lower()
    ]

@tree.command(name="summon", description="Commande Minecraft /summon avec autocomplétion avancée")
@app_commands.describe(entity="Sélectionnez l'entité à invoquer")
@app_commands.autocomplete(entity=autocomplete_entity)
@app_commands.describe(nbt="Ajoutez un NBT à l'entité (facultatif)")
@app_commands.autocomplete(nbt=autocomplete_nbt)  # Réutilisation de la fonction existante
async def summon_command(interaction: discord.Interaction, entity: str, nbt: str = None):
    command = f"/summon {entity}"
    if nbt:
        command += f" {nbt}"
    await interaction.response.send_message(command)


async def autocomplete_effect(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=effect, value=effect)
        for effect in EFFECTS
        if current.lower() in effect.lower()
    ]

@tree.command(name="effect", description="Applique un effet à un joueur ou une entité")
@app_commands.describe(player="Sélectionnez le joueur ou l'entité")
@app_commands.autocomplete(player=autocomplete_player)
@app_commands.describe(effect="Choisissez l'effet à appliquer")
@app_commands.autocomplete(effect=autocomplete_effect)
@app_commands.describe(duration="Durée de l'effet en secondes (défaut : 30)")
@app_commands.describe(amplifier="Niveau de l'effet (défaut : 1)")
@app_commands.describe(hide_particles="Masquer les particules (true/false)")
async def effect_command(
    interaction: discord.Interaction, 
    player: str, 
    effect: str, 
    duration: int = 30, 
    amplifier: int = 1, 
    hide_particles: bool = False
):
    hide_particles_text = "true" if hide_particles else "false"
    command = f"/effect give {player} {effect} {duration} {amplifier} {hide_particles_text}"
    await interaction.response.send_message(command)

async def autocomplete_teleport(interaction: discord.Interaction, current: str):
    # Autocomplétion pour les joueurs
    if current.lower().startswith("@") or current.lower() in roles_data.keys():
        return [
            app_commands.Choice(name=player, value=player)
            for player in roles_data.keys()
            if current.lower() in player.lower()
        ]
    # Autocomplétion pour les coordonnées
    elif current.replace(",", "").replace(".", "").isdigit():
        return [
            app_commands.Choice(name=f"Coordonnée: {current}", value=current)
            for x in range(-30000000, 30000000, 1000)  # Prise d'exemple pour les coordonnées
        ]
    return []
@tree.command(name="tp", description="Téléporte un joueur vers un autre joueur ou des coordonnées.")
@app_commands.describe(player="Sélectionnez le joueur ou entrez des coordonnées")
@app_commands.autocomplete(player=autocomplete_teleport)
async def tp_command(interaction: discord.Interaction, player: str, destination: str):
    # Vérifier si la destination est un joueur ou des coordonnées
    if destination in roles_data:
        command = f"/tp {player} {destination}"  # Téléportation d'un joueur vers un autre joueur
    else:
        # Téléportation vers des coordonnées, les coordonnées sont séparées par des virgules
        coords = destination.split(",")
        if len(coords) == 3:
            x, y, z = coords
            command = f"/tp {player} {x} {y} {z}"  # Téléportation vers les coordonnées
        else:
            await interaction.response.send_message("Les coordonnées doivent être sous la forme X,Y,Z.")
            return

    await interaction.response.send_message(command)

async def autocomplete_time(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name="day", value="day"),
        app_commands.Choice(name="night", value="night"),
        app_commands.Choice(name="set", value="set"),
        app_commands.Choice(name="query", value="query"),
        app_commands.Choice(name="add", value="add"),
    ]
@tree.command(name="time", description="Change ou consulte l'heure dans Minecraft.")
@app_commands.describe(time_command="Sélectionnez l'action à effectuer (ex: day, night, set <value>, add <value>)")
@app_commands.autocomplete(time_command=autocomplete_time)
async def time_command(interaction: discord.Interaction, time_command: str, value: str = None):
    if time_command == "day":
        command = "/time set day"
    elif time_command == "night":
        command = "/time set night"
    elif time_command == "set" and value:
        command = f"/time set {value}"  # Exemple: "/time set 1000"
    elif time_command == "add" and value:
        command = f"/time add {value}"  # Exemple: "/time add 5000"
    elif time_command == "query":
        command = "/time query daytime"
    else:
        await interaction.response.send_message("Commande invalide ou valeur manquante.")
        return
    
    await interaction.response.send_message(command)
async def autocomplete_weather(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name="clear", value="clear"),
        app_commands.Choice(name="rain", value="rain"),
        app_commands.Choice(name="thunder", value="thunder"),
    ]
@tree.command(name="weather", description="Change les conditions météorologiques dans Minecraft.")
@app_commands.describe(weather_condition="Choisissez la condition météorologique (clear, rain, thunder)")
@app_commands.autocomplete(weather_condition=autocomplete_weather)
async def weather_command(interaction: discord.Interaction, weather_condition: str):
    if weather_condition == "clear":
        command = "/weather clear"
    elif weather_condition == "rain":
        command = "/weather rain"
    elif weather_condition == "thunder":
        command = "/weather thunder"
    else:
        await interaction.response.send_message("Condition météorologique invalide.")
        return

    await interaction.response.send_message(command)

async def autocomplete_gamemode(interaction: discord.Interaction, current: str):
    # Liste des modes de jeu disponibles
    gamemodes = ["survival", "creative", "adventure", "spectator"]
    return [
        app_commands.Choice(name=mode.capitalize(), value=mode)
        for mode in gamemodes
        if current.lower() in mode.lower()
    ]

@tree.command(name="gamemode", description="Change le mode de jeu d'un joueur")
@app_commands.describe(player="Sélectionnez le joueur à modifier")
@app_commands.autocomplete(player=autocomplete_player)
@app_commands.describe(gamemode="Choisissez le mode de jeu")
@app_commands.autocomplete(gamemode=autocomplete_gamemode)
async def gamemode_command(interaction: discord.Interaction, player: str, gamemode: str):
    if gamemode not in ["survival", "creative", "adventure", "spectator"]:
        await interaction.response.send_message("Mode de jeu invalide.")
        return
    
    command = f"/gamemode {gamemode} {player}"
    await interaction.response.send_message(command)



@bot.event
async def on_ready():
    await tree.sync()
    print(f"{bot.user} est prêt !")

async def bot_run():
    while True:
        try:
            # Tentative de connexion à Discord
            await bot.start("MTI5NzgzMjcyMzY0NTMzNzYyMA.GYzBwo.BFrjcpbhncI2rzUr7JIweZ4VbbGY0iugYF6Jhk")
            break  # Si la connexion réussit, on sort de la boucle
        except Exception as e:
            print("Connexion à Discord impossible")
            print(f"Erreur : {e}")
            print("Réessai dans 2 secondes...")
            await asyncio.sleep(2)  # Attendre 2 secondes avant de réessayer

# Lancer la fonction avec asyncio
asyncio.run(bot_run())