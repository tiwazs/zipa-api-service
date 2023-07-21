/*
  Warnings:

  - Added the required column `updated_at` to the `AssignedSkillType` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Effect` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Faction` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Item` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `ItemSkill` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Skill` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `SkillEffect` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `SkillType` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Trait` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `TraitEffect` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Unit` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `UnitItem` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `UnitSkill` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `UnitTrait` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `AssignedSkillType` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Effect` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Faction` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Item` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `ItemSkill` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Skill` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `SkillEffect` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `SkillType` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Trait` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `TraitEffect` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `Unit` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `UnitItem` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `UnitSkill` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;

-- AlterTable
ALTER TABLE `UnitTrait` ADD COLUMN `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    ADD COLUMN `updated_at` DATETIME(3) NOT NULL;
