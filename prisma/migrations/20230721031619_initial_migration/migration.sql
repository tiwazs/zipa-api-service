-- CreateTable
CREATE TABLE `Faction` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `identity` VARCHAR(191) NULL,
    `aspects` VARCHAR(191) NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Unit` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `vitality` DOUBLE NOT NULL,
    `range` DOUBLE NOT NULL,
    `damage` DOUBLE NOT NULL,
    `armor` DOUBLE NOT NULL,
    `magic_armor` DOUBLE NOT NULL,
    `essence` DOUBLE NOT NULL,
    `agility` DOUBLE NOT NULL,
    `hit_chance` DOUBLE NOT NULL,
    `evasion` DOUBLE NOT NULL,
    `hit_rate` DOUBLE NOT NULL,
    `movement` DOUBLE NOT NULL,
    `ammo` DOUBLE NOT NULL,
    `shield` DOUBLE NOT NULL,
    `tier` INTEGER NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `SkillType` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Skill` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `physical_damage` VARCHAR(191) NULL,
    `magical_damage` VARCHAR(191) NULL,
    `healing` VARCHAR(191) NULL,
    `essence_recovery` VARCHAR(191) NULL,
    `range` VARCHAR(191) NULL,
    `area_of_effect` VARCHAR(191) NULL,
    `essence_cost` VARCHAR(191) NULL,
    `vitality_cost` VARCHAR(191) NULL,
    `cooldown` DOUBLE NOT NULL,
    `channeled` BOOLEAN NOT NULL,
    `target` ENUM('NONE', 'SELF', 'ALLY', 'ENEMY', 'AROUND', 'POINT', 'AREA', 'ALL') NOT NULL DEFAULT 'ENEMY',
    `skill_on` ENUM('INSTANT', 'OVER_TIME', 'DURING_CHANNEL', 'AFTER_CHANNEL', 'DELAYED') NOT NULL DEFAULT 'INSTANT',

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Trait` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `cooldown` DOUBLE NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Item` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `rarity` ENUM('COMMON', 'UNCOMMON', 'RARE', 'EPIC', 'LEGENDARY') NOT NULL DEFAULT 'COMMON',
    `magic_effectiveness` VARCHAR(191) NULL,
    `physical_damage` VARCHAR(191) NULL,
    `magical_damage` VARCHAR(191) NULL,
    `healing` VARCHAR(191) NULL,
    `essence_recovery` VARCHAR(191) NULL,
    `vitality` VARCHAR(191) NULL,
    `range` VARCHAR(191) NULL,
    `damage` VARCHAR(191) NULL,
    `armor` VARCHAR(191) NULL,
    `magic_armor` VARCHAR(191) NULL,
    `essence` VARCHAR(191) NULL,
    `agility` VARCHAR(191) NULL,
    `hit_chance` VARCHAR(191) NULL,
    `evasion` VARCHAR(191) NULL,
    `hit_rate` VARCHAR(191) NULL,
    `movement` VARCHAR(191) NULL,
    `ammo` VARCHAR(191) NULL,
    `shield` VARCHAR(191) NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Effect` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `magic_effectiveness` VARCHAR(191) NULL,
    `physical_damage` VARCHAR(191) NULL,
    `magical_damage` VARCHAR(191) NULL,
    `healing` VARCHAR(191) NULL,
    `essence_recovery` VARCHAR(191) NULL,
    `vitality` VARCHAR(191) NULL,
    `range` VARCHAR(191) NULL,
    `damage` VARCHAR(191) NULL,
    `armor` VARCHAR(191) NULL,
    `magic_armor` VARCHAR(191) NULL,
    `essence` VARCHAR(191) NULL,
    `agility` VARCHAR(191) NULL,
    `hit_chance` VARCHAR(191) NULL,
    `evasion` VARCHAR(191) NULL,
    `hit_rate` VARCHAR(191) NULL,
    `movement` VARCHAR(191) NULL,
    `ammo` VARCHAR(191) NULL,
    `shield` VARCHAR(191) NULL,
    `barrier` DOUBLE NULL,
    `max_stack` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `AssignedSkillType` (
    `id` VARCHAR(191) NOT NULL,
    `skill_id` VARCHAR(191) NOT NULL,
    `skill_type_id` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitSkill` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `skill_id` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitItem` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `item_id` VARCHAR(191) NOT NULL,
    `quantity` DOUBLE NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `ItemSkill` (
    `id` VARCHAR(191) NOT NULL,
    `item_id` VARCHAR(191) NOT NULL,
    `skill_id` VARCHAR(191) NOT NULL,
    `essence_cost` DOUBLE NOT NULL,
    `cooldown` DOUBLE NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitTrait` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `SkillEffect` (
    `id` VARCHAR(191) NOT NULL,
    `skill_id` VARCHAR(191) NOT NULL,
    `effect_id` VARCHAR(191) NOT NULL,
    `duration` DOUBLE NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `TraitEffect` (
    `id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `effect_id` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Unit` ADD CONSTRAINT `Unit_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `AssignedSkillType` ADD CONSTRAINT `AssignedSkillType_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `AssignedSkillType` ADD CONSTRAINT `AssignedSkillType_skill_type_id_fkey` FOREIGN KEY (`skill_type_id`) REFERENCES `SkillType`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSkill` ADD CONSTRAINT `UnitSkill_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSkill` ADD CONSTRAINT `UnitSkill_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitItem` ADD CONSTRAINT `UnitItem_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitItem` ADD CONSTRAINT `UnitItem_item_id_fkey` FOREIGN KEY (`item_id`) REFERENCES `Item`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ItemSkill` ADD CONSTRAINT `ItemSkill_item_id_fkey` FOREIGN KEY (`item_id`) REFERENCES `Item`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `ItemSkill` ADD CONSTRAINT `ItemSkill_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitTrait` ADD CONSTRAINT `UnitTrait_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitTrait` ADD CONSTRAINT `UnitTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SkillEffect` ADD CONSTRAINT `SkillEffect_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SkillEffect` ADD CONSTRAINT `SkillEffect_effect_id_fkey` FOREIGN KEY (`effect_id`) REFERENCES `Effect`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `TraitEffect` ADD CONSTRAINT `TraitEffect_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `TraitEffect` ADD CONSTRAINT `TraitEffect_effect_id_fkey` FOREIGN KEY (`effect_id`) REFERENCES `Effect`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
