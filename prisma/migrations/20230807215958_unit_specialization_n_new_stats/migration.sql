/*
  Warnings:

  - You are about to drop the column `unit_id` on the `SkillSummon` table. All the data in the column will be lost.
  - You are about to drop the `FactionUnit` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Unit` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `UnitItem` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `UnitSkill` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `UnitTrait` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `unit_specialization_id` to the `SkillSummon` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE `FactionUnit` DROP FOREIGN KEY `FactionUnit_faction_id_fkey`;

-- DropForeignKey
ALTER TABLE `FactionUnit` DROP FOREIGN KEY `FactionUnit_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `SkillSummon` DROP FOREIGN KEY `SkillSummon_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitItem` DROP FOREIGN KEY `UnitItem_item_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitItem` DROP FOREIGN KEY `UnitItem_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitSkill` DROP FOREIGN KEY `UnitSkill_skill_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitSkill` DROP FOREIGN KEY `UnitSkill_unit_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitTrait` DROP FOREIGN KEY `UnitTrait_trait_id_fkey`;

-- DropForeignKey
ALTER TABLE `UnitTrait` DROP FOREIGN KEY `UnitTrait_unit_id_fkey`;

-- AlterTable
ALTER TABLE `Item` ADD COLUMN `dexterity_requirement` DOUBLE NOT NULL DEFAULT 0,
    ADD COLUMN `faith_requirement` DOUBLE NOT NULL DEFAULT 0,
    ADD COLUMN `mind_requirement` DOUBLE NOT NULL DEFAULT 0,
    ADD COLUMN `strength_requirement` DOUBLE NOT NULL DEFAULT 0,
    ADD COLUMN `weight` DOUBLE NOT NULL DEFAULT 0;

-- AlterTable
ALTER TABLE `SkillEffect` ADD COLUMN `conditions` VARCHAR(191) NULL;

-- AlterTable
ALTER TABLE `SkillSummon` DROP COLUMN `unit_id`,
    ADD COLUMN `conditions` VARCHAR(191) NULL,
    ADD COLUMN `unit_specialization_id` VARCHAR(191) NOT NULL;

-- DropTable
DROP TABLE `FactionUnit`;

-- DropTable
DROP TABLE `Unit`;

-- DropTable
DROP TABLE `UnitItem`;

-- DropTable
DROP TABLE `UnitSkill`;

-- DropTable
DROP TABLE `UnitTrait`;

-- CreateTable
CREATE TABLE `UnitSpecialization` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NOT NULL,
    `vitality` DOUBLE NOT NULL,
    `range` DOUBLE NOT NULL,
    `strength` DOUBLE NOT NULL,
    `dexterity` DOUBLE NOT NULL,
    `mind` DOUBLE NOT NULL,
    `faith` DOUBLE NOT NULL,
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
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `FactionUnitSpecialization` (
    `id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitSpecializationSkill` (
    `id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `skill_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitSpecializationItem` (
    `id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `item_id` VARCHAR(191) NOT NULL,
    `quantity` DOUBLE NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitSpecializationTrait` (
    `id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `FactionUnitSpecialization` ADD CONSTRAINT `FactionUnitSpecialization_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionUnitSpecialization` ADD CONSTRAINT `FactionUnitSpecialization_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationSkill` ADD CONSTRAINT `UnitSpecializationSkill_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationSkill` ADD CONSTRAINT `UnitSpecializationSkill_skill_id_fkey` FOREIGN KEY (`skill_id`) REFERENCES `Skill`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationItem` ADD CONSTRAINT `UnitSpecializationItem_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationItem` ADD CONSTRAINT `UnitSpecializationItem_item_id_fkey` FOREIGN KEY (`item_id`) REFERENCES `Item`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationTrait` ADD CONSTRAINT `UnitSpecializationTrait_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitSpecializationTrait` ADD CONSTRAINT `UnitSpecializationTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SkillSummon` ADD CONSTRAINT `SkillSummon_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
