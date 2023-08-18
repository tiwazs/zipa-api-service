-- AlterTable
ALTER TABLE `Faction` MODIFY `identity` TEXT NULL,
    MODIFY `aspects` TEXT NULL;

-- AlterTable
ALTER TABLE `UnitSpecializationTrait` ADD COLUMN `conditions` VARCHAR(191) NULL;

-- CreateTable
CREATE TABLE `FactionTrait` (
    `id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `conditions` VARCHAR(191) NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `FactionTrait` ADD CONSTRAINT `FactionTrait_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `Faction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionTrait` ADD CONSTRAINT `FactionTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
